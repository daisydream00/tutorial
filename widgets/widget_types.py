import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("## Widgets that return string values")


st.markdown("### :material/list_alt: [`st.selectbox()`](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
        # default to the 1st option
        contact_str = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone")
        )

st.markdown(f"The value of variable `contact_str` is `'{contact_str}'` of `{type(contact_str)}`.")
with st.expander("Show documentation"):
    st.write(st.selectbox.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.radio()`](https://docs.streamlit.io/develop/api-reference/widgets/st.radio)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the 1st option
        genre_str = st.radio(
            "What's your favorite movie genre?",
            ["Comedy", "Drama", "Documentary"]
        )
        
st.markdown(f"The value of variable `genre_str` is `'{genre_str}'` of `{type(genre_str)}`.")
with st.expander("Show documentation"):
    st.write(st.radio.__doc__)

st.divider()

st.markdown("### :material/list_alt: [`st.text_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
    # default to an empty string
        name_str = st.text_input("Enter your username")
st.markdown(f"The value of variable `name_str` is `'{name_str}'` of `{type(name_str)}`.")


st.info("Simply typing inside the widget won't rerun its widget function to return a new value. An update is triggered either by clicking or tabbing out of the widget or by pressing `Enter`.", 
        icon="🚨")

with st.expander("Show documentation"):
    st.write(st.text_input.__doc__)

st.divider()
 
st.markdown("### :material/list_alt: [`st.text_area()`](https://docs.streamlit.io/develop/api-reference/widgets/st.text_area)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to an empty string
        txt_str = st.text_area("Text to analyze")
st.markdown(f"The value of variable `name_str` is<br>`'''{txt_str}'''`<br>of `{type(txt_str)}`",
            unsafe_allow_html=True)

st.info("Simply typing inside the widget won't rerun the widget function to return a new value. An update is triggered either by clicking or tabbing out of the widget or by pressing `Enter`.",
        icon="🚨")

with st.expander("Show documentation"):
    st.write(st.text_area.__doc__)





st.divider()

st.markdown("### Widgets that return list values")

st.markdown("### :material/list_alt: [`st.multiselect()`](https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect)")

st.markdown("<br/>", unsafe_allow_html=True)
 
with st.container(border=True):
    with st.echo("below"):
        # default to an empty list
        colors_list = st.multiselect(
            "What are your favorite colors",
            ["Green", "Yellow", "Red", "Blue"]
        )

st.markdown(f"The value of variable `colors_list` is `{colors_list}` of `{type(colors_list)}`.")
with st.expander("Show documentation"):
    st.write(st.multiselect.__doc__)
st.divider()

st.markdown("### Widgets that return numeric values")
 

st.markdown("### :material/list_alt: [`st.slider()`](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_float = st.slider(
            'Choose a value',
            min_value=10.0, max_value=50.0
        )

st.markdown(f"The value of variable `slider_float` is `{slider_float}` of `{type(slider_float)}`.")

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_int = st.slider(
            'Choose a value',
            min_value=10, max_value=50
        )

st.markdown(f"The value of variable `slider_int` is `{slider_int}` of `{type(slider_int)}`.")

st.divider()

st.markdown("""Passing a tuple/list of two numeric values as the `value` argument creates a range selector.

Make sure that the types of the numberic values is consistent of those of the maximum and minimum values."""
)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_float_range = st.slider(
            'Choose two values', min_value=10.0, max_value=50.0,
            value=(10.0, 20.0)
        )
st.markdown(f"The value of variable `slider_float_range` is `{slider_float_range}` of `{type(slider_float_range)}`.")

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_int_range = st.slider(
            'Choose two values', min_value=10, max_value=50, 
            value=[30, 40]
        )
st.markdown(f"The value of variable `slider_int_range` is `{slider_int_range}` of `{type(slider_int_range)}`.")


with st.expander("Show documentation"):
    st.write(st.slider.__doc__)

st.divider()

st.markdown("### :material/list_alt: [`st.number_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.number_input)")

st.markdown("<br/>", unsafe_allow_html=True)
 

with st.container(border=True):
    with st.echo("below"):
        input_float = st.number_input('Input a value')

st.markdown(f"The value of variable `input_float` is `{input_float}` of `{type(input_float)}`.")

with st.container(border=True):
    with st.echo("below"):
        input_int = st.number_input('Input a value', value=0)

st.markdown(f"The value of variable `input_int` is `{input_int}` of `{type(input_int)}`.")

with st.expander("Show documentation"):
    st.write(st.number_input.__doc__)
st.divider()

st.markdown("### Widgets that return Boolean values")

st.markdown("### :material/list_alt: [`st.checkbox()`](https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox)")

st.markdown("<br/>", unsafe_allow_html=True)
 
with st.container(border=True):
    with st.echo("below"):
        # default to False
        agree_bool = st.checkbox("I agree")
st.markdown(f"The value of variable `agree_bool` is `{agree_bool}` of `{type(agree_bool)}`.")
with st.expander("Show documentation"):
    st.write(st.checkbox.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.toggle()`](https://docs.streamlit.io/develop/api-reference/widgets/st.toggle)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
        # default to False
        activated_bool = st.toggle("Activate feature")
st.markdown(f"The value of variable `activated_bool` is `{activated_bool}` of `{type(activated_bool)}`.")
with st.expander("Show documentation"):
    st.write(st.toggle.__doc__)
st.divider()

st.markdown("### Widgets that return date/time values (Optional)")

st.markdown("### :material/list_alt: [`st.time_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.time_input)")

st.markdown("<br/>", unsafe_allow_html=True)

from datetime import datetime

with st.container(border=True):
    with st.echo("below"):
        # default to the current time
        t_time = st.time_input("Set an alarm for", value = datetime.now(), step=60)
st.markdown(f"The value of variable `t_time` is `{t_time}` of `{type(t_time)}`.")
with st.expander("Show documentation"):
    st.write(st.time_input.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.date_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.date_input)")

st.markdown("<br/>", unsafe_allow_html=True)
 

with st.container(border=True):
    with st.echo("below"):
        # default to the current date
        bd_date = st.date_input("When's your birthday?")
st.markdown(f"The value of variable `bd_date` is `{bd_date}` of `{type(bd_date)}`.")
with st.expander("Show documentation"):
    st.write(st.date_input.__doc__)
