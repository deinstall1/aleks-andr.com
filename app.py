from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import openai

app = Flask(__name__)
CORS(app)

# Настрой свой путь к базе и ключ OpenAI
DB_PATH = '/Users/aleksandrandrienko/HealthData/DBs/garmin_activities.db'
OPENAI_API_KEY = 'sk-...'

@app.route('/api/activities')
def get_activities():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities ORDER BY start_time DESC LIMIT 10;")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/api/plan', methods=['POST'])
def get_plan():
    data = request.json
    activity_info = data.get('activity_info', '')
    prompt = f"Составь план питания для такой тренировки: {activity_info}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # или "gpt-4o"
        messages=[{"role": "user", "content": prompt}]
    )
    plan = response.choices[0].message.content
    return jsonify({'plan': plan})

@app.route('/api/update', methods=['POST'])
def update_data():
    # Здесь можно добавить запуск обновления GarminDB, а пока — тестовый ответ:
    return jsonify({'status': 'ok', 'output': 'Данные обновлены!'})

if __name__ == '__main__':
    app.run(debug=True)