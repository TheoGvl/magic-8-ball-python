import flet as ft
import random

def main(page: ft.Page):
    # Ρυθμίσεις του παραθύρου
    page.title = "Μαγική 8-Ball"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Η Λίστα με τις πιθανές απαντήσεις της μπάλας
    apantiseis = [
        "Είναι απολύτως βέβαιο!",
        "Χωρίς καμία αμφιβολία.",
        "Μπορείς να βασιστείς σε αυτό.",
        "Οι οιωνοί δείχνουν ναι.",
        "Ρώτα ξανά αργότερα...",
        "Καλύτερα να μην σου πω τώρα.",
        "Συγκεντρώσου και ρώτα ξανά.",
        "Μην υπολογίζεις σε αυτό.",
        "Η απάντησή μου είναι όχι.",
        "Πολύ χλωμό το βλέπω..."
    ]

    # --- Η συνάρτηση που τρέχει όταν πατάμε το κουμπί ---
    def rwta_ti_mpala(e):
        erwtisi = erwtisi_input.value
        
        # Ελέγχουμε αν ο χρήστης άφησε το κουτί άδειο
        if not erwtisi:
            apantisi_text.value = "Πρέπει να ρωτήσεις κάτι πρώτα!"
            apantisi_text.color = "red"
        else:
            # Διαλέγει στην τύχη ΜΙΑ απάντηση από τη λίστα
            tyxaia_apantisi = random.choice(apantiseis)
            apantisi_text.value = tyxaia_apantisi
            apantisi_text.color = "cyan"
            
        page.update()

    
    # Τίτλος
    titlos = ft.Text("Μαγική 8-Ball", size=40, weight=ft.FontWeight.BOLD)
    
    # Το κουτί που θα γράφεις την ερώτηση
    erwtisi_input = ft.TextField(
        label="Ρώτα κάτι που απαντιέται με Ναι ή Όχι...", 
        width=300,
        text_align=ft.TextAlign.CENTER
    )
    
    # Το κουμπί
    btn = ft.Button(
        content=ft.Text("Ρώτα τη Μπάλα!", size=20),
        on_click=rwta_ti_mpala,
        height=50
    )
    
    # Εδώ θα εμφανίζεται η μαντεψιά
    apantisi_text = ft.Text("Η απάντηση θα εμφανιστεί εδώ.", size=22, italic=True)

    # Βάζουμε τα πάντα μέσα στη σελίδα με λίγο κενό ανάμεσα
    page.add(
        titlos,
        ft.Divider(height=20, color="transparent"),
        erwtisi_input,
        btn,
        ft.Divider(height=30, color="transparent"),
        apantisi_text
    )

ft.run(main)