# faq_bot.py

def faq_bot(question):
    faq = {
        "where is the library": "The library is located in Block A, first floor.",
        "what are library timings": "Library timings are from 9 AM to 6 PM.",
        "who is the principal": "Dr. XYZ is the current principal of the college.",
        "how to apply for leave": "You can apply for leave through the student portal."
    }
    
    question = question.lower()
    for q, a in faq.items():
        if q in question:
            return a
    return "Sorry, I don't know the answer. Please contact admin."

