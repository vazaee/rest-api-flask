def normalize_path_params(cidade=None, estrelas_min = 0, estrelas_max = 5, diaria_min = 0,
                          diaria_max = 10000, limit = 50, offset = 0, **dados):
    args = {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset
    }
    
    if cidade:
        args['cidade'] = cidade
        return args

    return args

consulta_sem_cidade = "SELECT * FROM hoteis \
            WHERE (estrelas >= ? and estrelas <= ?) \
            AND (diaria >= ? and diaria <= ?) \
            LIMIT ? OFFSET ?"

consulta_com_cidade = "SELECT * FROM hoteis \
            WHERE (estrelas >= ? and estrelas <= ?) \
            AND (diaria >= ? and diaria <= ?) \
            AND (cidade = ?) LIMIT ? OFFSET ?"