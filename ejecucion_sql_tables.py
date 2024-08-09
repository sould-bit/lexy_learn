#%%
import mysql.connector 

#importamos la funcion de la coneccion a la BD
from conector_sql import connect_db

import pandas as pd 
from mysql.connector import Error
from datetime import datetime, timedelta


def get_next_element(user_id,is_premium,element_type):
    """
    esta funcion obtiene las palabras de la base de datos distinguiendo si el usuario es premiun o no,  
    user_id: el id del usuario
    is_premium: si el usuario es premium o no
    element_type: el tipo de elemento que se quiere obtener(word, slang)
    
    """
    
    
    conn = connect_db()

    cursor = conn.cursor()

    if element_type == 'word':
        table = 'words'
        user_table = 'user_words'
        id_field = 'word_id'
        level_condition = "('A1', 'A2')" if not is_premium else "('A1', 'A2', 'B1', 'B2', 'C1')"
        
        # Obtener elementos para revisión
        query = f'''
            SELECT w.{id_field},word,phonetic,traslation
            FROM {table} w
            JOIN {user_table} uw ON w.{id_field} = uw.{id_field}
            WHERE uw.user_id = %s AND uw.next_review_date <= %s
        '''
        
    elif element_type == 'american_slang'and is_premium:
        table = 'american_slang'
        user_table = 'user_slang'
        id_field = 'slang_id'
    
        # Obtener elementos para revisión
        query = f'''
            SELECT w.{id_field},phrase,context,phonetic,traslation
            FROM {table} w
            JOIN {user_table} uw ON w.{id_field} = uw.{id_field}
            WHERE uw.user_id = %s AND uw.next_review_date <= %s
        '''
    cursor.execute(query, (user_id, datetime.now()))
    elements_to_review = cursor.fetchall()

    if not elements_to_review and element_type =='american_slang':
         # Verificar si ya se han asignado palabras durante el período de estudio de 7 días
        query = f'''
            SELECT u.{id_field}, a.phrase ,a.context ,a.phonetic ,a.traslation 
            FROM {user_table} u
            JOIN {table} a on u.{id_field} = a.{id_field}
            WHERE user_id = %s AND assigned_date >= %s
        '''
        cursor.execute(query, (user_id, datetime.now() - timedelta(days=7)))
        current_words = cursor.fetchall()
    
    elif not elements_to_review and element_type =='word':
        # Verificar si ya se han asignado palabras durante el período de estudio de 7 días
        query = f'''
            SELECT u.{id_field}, a.word ,a.phonetic ,a.traslation 
            FROM {user_table} u
            JOIN {table} a on u.{id_field} = a.{id_field}
            WHERE user_id = %s AND assigned_date >= %s
        '''
        cursor.execute(query, (user_id, datetime.now() - timedelta(days=7)))
        current_words = cursor.fetchall()
    
    if current_words:
        elements_to_review = current_words
    else:
    
    
    
        # Obtener nuevos elementos si no hay elementos para revisión
        if element_type == 'word':
            query = f'''
               SELECT {id_field},word ,phonetic ,traslation 
               FROM {table}
               {f"WHERE level IN {level_condition}"}
               ORDER BY RAND()
               LIMIT 10
                '''
            cursor.execute(query)
            new_elements = cursor.fetchall()
            for element_id, element,phonetic_element,traslation_element in new_elements:
                print(f"element_id:  {element_id} element : {element} phonetic :{phonetic_element} traslation :{traslation_element}")
                query = f'''
                    INSERT IGNORE INTO {user_table} (user_id, {id_field}, next_review_date, assigned_date)
                    VALUES (%s, %s, %s,%s)
                '''
                cursor.execute(query, (user_id, element_id, datetime.now(),datetime.now()))
            conn.commit()
            elements_to_review = new_elements
            
           
        elif element_type == 'american_slang':
            query = f'''
               SELECT {id_field},phrase,context,phonetic,traslation
               FROM {table}
               ORDER BY RAND()
               LIMIT 3
           '''
            cursor.execute(query)
            new_elements = cursor.fetchall()
            for element_id, element,context_element,phonetic_element,traslation_element in new_elements:
                print(f"element_id:  {element_id} element : {element} conetx_elemet: {context_element} phonetic :{phonetic_element} traslation :{traslation_element}")
                query = f'''
                    INSERT IGNORE INTO {user_table} (user_id, {id_field}, next_review_date, assigned_date)
                    VALUES (%s, %s, %s,%s)
                '''
                cursor.execute(query, (user_id, element_id, datetime.now(),datetime.now()))
            conn.commit()
            elements_to_review = new_elements
        
    #actualizamos las tablas si se cumplen las condiciones de la funcion update_review_dates    
    update_review_dates(user_id,element_type ,[word_id[0] for word_id in elements_to_review])
    tuples = [element[1:] for element in elements_to_review]
    conn.close()
    return cleaned_output(tuples,element_type)


def update_review_dates(user_id, element_type,element_ids):
    conn = connect_db()
    cursor = conn.cursor()

    if element_type == 'word':
        user_table = 'user_words'
        id_field = 'word_id'
        learn_table ='learned_words'
    elif element_type == 'american_slang':
        user_table = 'user_slang'
        id_field = 'slang_id'
        learn_table ='learned_slang'
    

    for element_id in element_ids:
        query = f'''
            UPDATE {user_table}
            SET next_review_date = CASE
                WHEN review_count <=  100 THEN %s + INTERVAL 1 DAY
            END,
            review_count = review_count + 1
            WHERE user_id = %s AND {id_field} = %s
        '''
        cursor.execute(query, (datetime.now(), user_id, element_id))
        conn.commit()
            # Mover a la tabla de palabras aprendidas si se ha revisado 7 veces y han pasado 7 dias 
        query = f'''
            INSERT INTO {learn_table} (user_id, {id_field}, learned_date)
            SELECT user_id, {id_field}, %s
            FROM {user_table}
            WHERE user_id = %s AND review_count >= 7 AND assigned_date <= %s
        '''
        cursor.execute(query, (datetime.now(), user_id, datetime.now() - timedelta(days=7) ))
        conn.commit()
        # Eliminar de la tabla de palabras en revisión
        query = f'''
            DELETE FROM {user_table}
            WHERE user_id = %s AND review_count >= 7 AND assigned_date <= %s
            
        
        '''
        cursor.execute(query, (user_id, datetime.now() - timedelta(days=7)))
        conn.commit()
    conn.close()


def cleaned_output(elemnets,tipe):
    '''limpia los elementos de las tuplas args
    elements : la lista de tuplas con las palabras 
    tipe : el tipo de elemento (word o american_slang)  
    '''
    if tipe == 'american_slang':
        sentences = []
        for element in elemnets:
            phrase, context, phonetic, translation = element
            sentence = f"Element:   - {phrase}\nContext:  - {context}\nPhonetic:  - {phonetic}\nTraslate:  - {translation}"
            sentences.append(sentence)
        return sentences 
    
    elif tipe == 'word':
        sentences = []
        for element in elemnets:
            phrase,phonetic, translation = element
            sentence = f"Element:   - {phrase}\nPhonetic:  - {phonetic}\nTraslate:  - {translation}"
            sentences.append(sentence)
        return sentences
    
