# Programa para gerar comandos SQL a partir de um arquivo .txt contendo perguntas e respostas

# Mapeamento entre áreas de negócio e seus IDs
business_area_mapping = {
    "Cibersegurança": 1,
    "Criptomoedas": 2,
    "Gestão de TI": 3,
    "Dados": 4,
    "Programação": 5,
    "Design/Jogos Digitais": 6,
    "Inteligência Artificial": 7
}

# Função para processar o arquivo .txt
def process_file(file_path):
    questions = []
    answers = []
    question_id = 0

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith(tuple(str(i) + "." for i in range(1, 13))):  # Identifica uma pergunta
                question_id += 1
                question_text = line.split(".", 1)[1].strip()
                questions.append((question_id, 1, question_text, 1, question_id))  # survey_id é sempre 1
            elif line.startswith(tuple("abcdefg)")):  # Identifica uma resposta
                answer_parts = line.split("(")
                answer_text = answer_parts[0].strip()
                business_area = answer_parts[1].replace(")", "").strip()
                business_area_id = business_area_mapping.get(business_area, None)
                answers.append((len(answers) + 1, 1, answer_text, len(answers) % 7 + 1, question_id, business_area_id))

    return questions, answers

# Função para gerar os comandos SQL
def generate_sql(questions, answers):
    # Comandos SQL para SurveyQuestion
    survey_question_sql = "INSERT INTO SurveyQuestion (id, status, description, survey_id, \"order\") VALUES\n" + ",\n".join(
        [f"({q[0]}, {q[1]}, '{q[2]}', {q[3]}, {q[4]})" for q in questions]
    ) + ";"

    # Comandos SQL para SurveyAnswer
    survey_answer_sql = "INSERT INTO SurveyAnswer (id, status, description, \"order\", survey_question_id, business_area_id) VALUES\n" + ",\n".join(
        [f"({a[0]}, {a[1]}, '{a[2]}', {a[3]}, {a[4]}, {a[5]})" for a in answers]
    ) + ";"

    return survey_question_sql, survey_answer_sql

# Caminho do arquivo .txt
file_path = "/Users/sergiosousa/work/python-vozes-na-tech/SQL/feed/perguntas_respostas.txt"

# Processar o arquivo e gerar os comandos SQL
questions, answers = process_file(file_path)
survey_question_sql, survey_answer_sql = generate_sql(questions, answers)

# Exibir os comandos SQL gerados
print("SurveyQuestion SQL:\n", survey_question_sql)
print("\nSurveyAnswer SQL:\n", survey_answer_sql)
