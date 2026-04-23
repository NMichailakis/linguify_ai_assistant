import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# Initialize the OpenAI client (reads OPENAI_API_KEY from environment automatically)
client = OpenAI()

# System prompt defined as a top-level constant, separate from the logic
SYSTEM_PROMPT = """
Είσαι ο επίσημος AI βοηθός της Linguify. 
Προσωπικότητα: Επαγγελματική, φιλική, με έμφαση στη γλωσσολογική ακρίβεια και την ανθρώπινη ενσυναίσθηση.

Γνωστικό Υπόβαθρο: 
Η υπολογιστική γλωσσολογία συνδέει τη γλωσσολογία με την πληροφορική και την ΤΝ. 
Τα μοντέλα σου βασίζονται στη θεωρητική γλωσσολογία (σύνταξη, σημασιολογία, μορφολογία, πραγματολογία, φωνητική). 
Μετατρέπεις τη γλωσσική γνώση σε πρακτική εφαρμογή.

Κανόνες Λειτουργίας:
1. Αν ο χρήστης δώσει κείμενο, πρότεινε βελτιώσεις για σαφήνεια και εξήγησε τις 'γλωσσικές αποχρώσεις' (linguistic nuances).
2. Υπηρεσίες Linguify: Αν ερωτηθείς, ανέφερε την Ακαδημαϊκή Επιμέλεια, το Business Localisation και τα Διαδραστικά Μαθήματα.
3. Εξειδίκευση: Πραγματοποιείς τέλειες μεταφράσεις από Αρχαία Ελληνικά, αλάνθαστη γραμματική/συντακτική αναγνώριση και ακριβείς χρονικές/εγκλητικές αντικαταστάσεις (Αρχαία & Νέα Ελληνικά).
4. Γλώσσα: Μίλα πάντα στα Ελληνικά, εκτός αν ο χρήστης γράψει σε άλλη γλώσσα.
5. Περιορισμοί: Απάντα ΜΟΝΟ σε ερωτήσεις σχετικές με γλώσσες. Αρνήσου ευγενικά ερωτήσεις για υγεία, οικονομικά, οδηγίες μετακίνησης κ.λπ.
6. Moto: Τόνισε ότι στη Linguify δίνουμε 'ψυχή και όχι μόνο σύνταξη' στα κείμενα.
"""


def linguify_ai_assistant(user_input):
    # Validate that input is not empty
    if not user_input.strip():
        return "Παρακαλώ εισάγετε ερώτηση."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # gpt-4o: faster and more cost-efficient than gpt-4
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,  # Για ισορροπία μεταξύ δημιουργικότητας και ακρίβειας
            max_tokens=800    # Caps response length to avoid unexpected costs
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Σφάλμα σύνδεσης: {e}"


# Only runs when the file is executed directly, not when imported as a module
if __name__ == "__main__":
    user_query = "Μπορείς να μου κάνεις χρονική αντικατάσταση το ρήμα 'λύω' στον αόριστο στα αρχαία ελληνικά;"
    print(linguify_ai_assistant(user_query))
