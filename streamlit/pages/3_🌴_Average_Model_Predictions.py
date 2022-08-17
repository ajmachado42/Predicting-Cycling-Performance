# streamlit run [file]
# https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b

import streamlit as st

st.set_page_config(
    page_title="Average Model", 
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Average Model")

st.header('Marin Century Classic (August 06, 2022)')

### Average Model

def main_avg():
    html_temp = """
    <div class='tableauPlaceholder' id='viz1660605750863' style='position: relative'>
    <noscript>
    <a href='#'>
    <img alt='Weather &amp; Elevation - Average Model ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PredictingCyclingMetrics-AverageModel-WeatherElevation&#47;WeatherElevation-AverageModel&#47;1_rss.png' style='border: none' />
    </a>
    </noscript>
    <object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='' />
    <param name='name' value='PredictingCyclingMetrics-AverageModel-WeatherElevation&#47;WeatherElevation-AverageModel' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PredictingCyclingMetrics-AverageModel-WeatherElevation&#47;WeatherElevation-AverageModel&#47;1.png' /> 
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' />
    <param name='filter' value='publish=yes' />
    </object>
    </div>                
    <script type='text/javascript'>                    
    var divElement = document.getElementById('viz1660605750863');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1220px';vizElement.style.height='887px';} 
    else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1220px';vizElement.style.height='887px';} 
    else { vizElement.style.width='100%';vizElement.style.height='1527px';}                     
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    </script>
    """
    st.components.v1.html(html_temp, width = 1500, height = 1220)

if __name__ == "__main__":    
    main_avg()   