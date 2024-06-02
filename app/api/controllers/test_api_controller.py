from app.core.OpenAIAssistant import OpenAIAssistant


class TestApiController:

    def __init__(self) -> None:
        self.assistant = OpenAIAssistant()


    def get_response_for_question(self, data: any):
        try:
            question = data.get('question')
            # Ejemplo de uso
            # Pregunta del usuario
            additional_instructions = "Sé amable y comprensiva con el usuario"
            response = self.assistant.ask_question_and_get_response(
                question, additional_instructions)

            # Si todo va bien, devuelve la respuesta
            return response
        except Exception as e:
            # Si ocurre un error, devuelve un mensaje indicando el error
            return f"Error al procesar la pregunta: {str(e)}"
