# importing required packages
import streamlit as st 
from st_pages import Page, show_pages, add_page_title

#st.sidebar.image('assets/PDF_Logo.jpg', use_column_width=True)

# Arranging orders, names and icons for pages including home page. 
show_pages([Page('app.py', 'Home', '🏠'),
            Page('pages/PDF_Merge.py', 'Merging PDFs', '➕'),
            Page('pages/PDF_Compression.py', 'Compressing PDF', '🗜️'),])

# Content for Home Page
st.title('PDF Editor Application')