from PySide6.QtWidgets import QFrame, QGridLayout, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QPalette

class STYLE():
    """
    PURPOSE

    Contains a library of stylesheets and functions to modify the style of the program.
    """
    # VARIABLES
    theme = True

    widgetHeight = 0

    def __init__(self):
        """
        PURPOSE

        Class constructor

        INPUT

        NONE

        RETURNS

        NONE
        """
        pass
    

    def setStylesheet(self, appObject):
        appObject.setStyleSheet(""" 
                 
            #controlPanelButton {
                font-size: 12pt;
                color: white;
                background-color: #007ACC;
                border-radius: 14px;
                padding: 6px 12px;
            }
            
            #program_exit {
                font-size: 12pt;
                color: white;
                background-color: red;
                border-radius: 14px;
                padding: 6px 12px;
            }
                                
            #shipwreckButton, #eDNAButton, #mappingButton, #floatButton{
                font-size: 12pt;
                color: white;
                background-color: #424242;
                border-radius: 14px;
                padding: 6px 12px;
            }
                                
            #eDNAInput {
                background-color: #424242;
                font-size: 16pt;
                color: white;                                    
            }
                                
            #toggleTimerButton {
                background-color: green;
            }     

            #timerLabel {
                font-size: 40px;
                color: white;
                padding-top: 4px;
            }                                   
                                
            QComboBox {
                background-color: #424242;               
            }
                            
            #shipNameDisplay {
                font-size: 40px;                    
            }

            QWidget {
                background-color: #161616;
                color: white;
            }  
                                
            QGroupBox {
                background-color: #212121
            }
                                
            QPushButton {
                background-color: #424242        
            }
                                
            #camera_feed_1, #camera_feed_2, #camera_feed_3, #camera_feed_4 {
                background-color: black;                    
            }
                                
            QStackedWidget, #control_panel_camera_widget, #control_panel_functions_widget,
            #buttonsPanel, #shipwreck_image_result_panel, #shipwreck_gui_panel, #database_display, 
            #float_panel_menu, #mapping_button_widget, #mapping_image_widget,
            #eDNA_panel_page_tab  {
                border: 1px solid #fafafa;
                border-radius: 10px;
            }       
                                
            #entryWidget {
                border: 1px solid #fafafa;                    
            }
                                
            #eDNA_samples_panel_groupbox QLabel{
                border: 1px solid #fafafa;
                color: #fafafa;
                font-size: 22px;
            }    
                                
            #fail_safe_species_label, #eDNA_sample_display{
                color: #fafafa;
                font-size: 20px;
            }    
                                
            QTableWidget {
                background-color: #212121;   
                color: #fafafa;                               
            }
                                
            QTableWidget::item {
                border: 1px solid #fafafa;
            }
                                
        """)