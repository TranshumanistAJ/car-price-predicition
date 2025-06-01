import streamlit as st

class MultiPage:
    """
    📜✨ The Tome of Many Roads ✨📜

    Behold the enchanted scroll that binds all realms of your mystical Car Prediction App!
    With this arcane class, one can summon multiple enchanted pages—each a portal to a unique vision—
    and traverse them through the mystical Sidebar of Navigation.

    Whether it's fortune-telling fuel efficiency or divining resale value, this tome keeps your journeys well-charted.
    """

    def __init__(self, app_name):
        """
        🔮 Ritual of Awakening 🔮

        Casts the first spell to breathe life into your magical interface.
        
        Parameters:
        app_name (str): The grand title of your app, to be etched atop the user’s viewing crystal.
        """
        self.pages = []  # The sacred ledger of realms
        self.app_name = app_name  # The name echoed across all dimensions

        st.set_page_config(
            page_title=self.app_name,  # Proclaims the app's title on the magic scroll (browser tab)
            page_icon="🧿"  # Wards off bugs with a mystical ward
        )

    def add_page(self, title, func):
        """
        🗺️ Carve a New Path 🗺️

        Adds a new page to your enchanted compendium of predictions.

        Parameters:
        title (str): The name of the page, as it shall appear in the mystical sidebar.
        func (function): The function—a spell—that breathes life into this page’s content.
        """
        self.pages.append({"title": title, "function": func})  # Inscribe a new route in the tome

    def run(self):
        """
        🧭 Begin the Journey 🧭

        Summons the chosen realm from the sidebar and conjures its contents.
        The user selects their path, and the app unveils its secrets accordingly.
        """
        st.title(self.app_name)  # Raise the banner of the realm

        page = st.sidebar.radio(
            "Choose Your Path",  # Whispered instructions to the traveler
            self.pages,
            format_func=lambda page: page["title"]  # Show only the realm's name
        )

        page["function"]()  # Invoke the magic of the selected path
