import streamlit as st


class MultiPage:
    """
    A class to create a multi-page Streamlit app.
    This class allows you to define multiple pages within the app
    and switch between them using a sidebar navigation menu.
    """
    def __init__(self, app_name):
        """
        Initializes the MultiPage app with the given name.

        Parameters:
        app_name (str): The name of the app to be displayed in the page title.
        """
        # Initialize the pages list to store the different pages in the app
        self.pages = []
        # Set the app's name, which will appear in the page title
        self.app_name = app_name

        # Set the page configuration including the title and icon
        st.set_page_config(
            page_title=self.app_name,  # Set the title of the page
            page_icon="💰"  # Set the page icon (💰)
        )

    def add_page(self, title, func):
        """
        Adds a new page to the app.

        Parameters:
        title (str): The title of the page as it will appear in the sidebar
        menu.
        func (function): The function that will render the content of the page.
        """
        # Append a dictionary containing the page title and corresponding
        # function to the pages list
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Runs the app by displaying the main title and setting up a sidebar menu
        for navigation.
        The selected page will be rendered based on the sidebar choice.
        """
        # Display the main title of the app at the top of the page
        st.title(self.app_name)

        # Create a sidebar radio button for page navigation, where users can
        # select pages
        # The `format_func` lambda is used to display only the page title in
        # the sidebar
        page = st.sidebar.radio(
            "Menu",  # Label for the sidebar menu
            self.pages,  # List of pages to display
            # Function to extract and display only the page title
            format_func=lambda page: page["title"]
        )

        # Call the function corresponding to the selected page
        page["function"]()
