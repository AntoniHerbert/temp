def transpiler(json_data, array_data):
    import json
    data = json.loads(json_data)

    global_array = [0] * len(array_data)

    for idx, item in enumerate(array_data):
        for json_item in data:
            json_name = json_item["name"]

            json_values = json_item["value"]
        

            if all(v in item for v in json_values) and json_name in item and all(json_name not in v for v in json_values) and all(v not in json_name for v in json_values):
                global_array[idx] = json_values
                break

    return global_array

def main():
    json_data = '''
    [
    {
        "exam": "ECO",
        "name": "date_predication",
        "type": "date",
        "value": [
        "1711304587"
        ]
    },
    {
        "exam": "ECO",
        "name": "disf_diastolica",
        "type": "categorical",
        "value": [
        "1"
        ]
    },
    {
        "exam": "ECO",
        "name": "ves",
        "type": "string",
        "value": [
        "1"
        ]
    },
    {
        "exam": "Holter",
        "name": "average_hr",
        "type": "number",
        "value": [
        "80"
        ]
    },
    {
        "exam": "Holter",
        "name": "dist_cond_atrio_vent",
        "type": "boolean",
        "value": [
        "false"
        ]
    },
    {
        "exam": "ECG",
        "name": "alt_prim",
        "type": "boolean",
        "value": [
        "false"
        ]
    }
    ]
    '''
    
    array_data = ['Sexo', 'BMI ', 'Cancer', 'HAS', 'DM2', 'Cardiopatia Outra',
       'Marcapasso', 'Sincope', 'Fibrilação/Flutter Atrial', 'I R Crônica',
       'DLP', 'Coronariopatia', 'Embolia Pulmonar', 'Ins Cardiaca ', 'AVC',
       'DVP', 'TSH', 'Tabagismo', 'Alcoolismo', 'Sedentarismo', 'FC',
       'Alt Prim', 'Pausa > 3s ', 'ESV', 'EV', 'TVMNS', 'Area Elet inativa',
       'Dist Cond AtrioVent', 'Disf Nodulo Sinusal', 'Fibri/Flutter Atrial',
       'FC media', 'TVS', 'TVMNS.1', 'EV.1', 'EVTotal', 'AE diam.', 'VED',
       'VES', 'FE Teicholz', 'Deficit Seg', 'Rassi pontos', 'CDI ', 'Ablações',
       'Amiodarona', 'Idade Holter', 'Rassi escore_baixo',
       'Rassi escore_intermediario', 'Diretriz 2005_A', 'Diretriz 2005_B1',
       'Diretriz 2005_B2', 'Classificação_Normal', 'Classificação_Disf Leve',
       'Classificação_Disf Moderada', 'Dist Cond AtrioVent _0',
       'Dist Cond InterVent _2', 'disf_diastolica_1', 'Disf Diastolica_0',
       'Disf Diastolica_2', 'NYHA_1', 'NYHA_2', 'NYHA_0', 'NYHA_3',
       'TendQ - 5º Percentil', 'TpeakQ - 5º Percentil', '% - Qtend/TendQ > 1',
       '% - QTpeak/TpeakQ > 1', '98% - Qtend/TendQ', '98% - QTpeak/TpeakQ',
       'Tp-Te (ms) - 5º Percentil', 'Obito_MS']
    
    print(transpiler(json_data, array_data))
    


if __name__ == "__main__":
    main()