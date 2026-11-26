# IT-қолдау өтінімдерін тіркеу жүйесі (Lab 12)

Django негізінде жасалған IT-қолдау өтінімдерін қабылдау және бақылау веб-қосымшасы.

## Жергілікті іске қосу (PyCharm / Terminal)
1. Виртуалды ортаны құрыңыз және іске қосыңыз:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
2. Тәуелділіктерді орнатыңыз:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env.example` негізінде `.env` файлын тексеріңіз.
4. Миграцияларды қолданып, серверді іске қосыңыз:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
