# Quiz API - Django & DRF

¡Bienvenido a la mejor API de quizzes construida con Django y Django REST Framework!

## Características
- Gestión completa de Quizzes, Preguntas y Opciones (Choices)
- Validación automática de respuestas
- Panel de administración amigable
- API RESTful navegable
- Estructura profesional y escalable

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPO>
   cd Lab08/quiz_api
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En Linux/Mac
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Accede a la API:**
   - Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Endpoints:
     - Quizzes: `/api/choices/quizzes/`
     - Questions: `/api/choices/questions/`
     - Choices: `/api/choices/choices/`
   - Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Estructura del Proyecto
```
quiz_api/
├── quizzes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── quiz_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## Uso de la API

### Crear un Quiz
POST `/api/choices/quizzes/`
```json
{
  "title": "Mi primer quiz",
  "description": "Descripción opcional"
}
```

### Crear una Pregunta
POST `/api/choices/questions/`
```json
{
  "quiz": 1,
  "text": "¿Cuál es la capital de Francia?"
}
```

### Crear una Opción (Choice)
POST `/api/choices/choices/`
```json
{
  "question": 1,
  "text": "París",
  "is_correct": true
}
```

### Validar Respuestas
POST `/api/choices/quizzes/{quiz_id}/validate/`
```json
{
  "answers": [
    {"question_id": 1, "choice_id": 2},
    {"question_id": 2, "choice_id": 5}
  ]
}
```

## Licencia
MIT

---

¡Contribuciones y sugerencias son bienvenidas! Si tienes dudas, abre un issue o contacta al autor.
