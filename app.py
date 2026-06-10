from scripts.generation import generate_answer
import gradio as gr


def answer_question(query):
    return generate_answer(query)


demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        label="Ask a question",
        placeholder="How can FGLI students find community at Northwestern?"
    ),
    outputs=gr.Markdown(label="Answer")
)

if __name__ == "__main__":
    demo.launch()