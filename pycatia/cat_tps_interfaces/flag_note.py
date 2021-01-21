#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class FlagNote(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FlagNote
                | 
                | Interface for the TPS Flag Note object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.flag_note = com_object

    @property
    def flag_note_text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlagNoteText() As CATBSTR
                | 
                |     Retrieves or sets Flag Text.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned Flag text.

        :return: str
        :rtype: str
        """

        return self.flag_note.FlagNoteText

    @flag_note_text.setter
    def flag_note_text(self, value: str):
        """
        :param str value:
        """

        self.flag_note.FlagNoteText = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Text() As CATBSTR
                | 
                |     Retrieves or sets Flag Text Representation.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for graphical representation.

        :return: str
        :rtype: str
        """

        return self.flag_note.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.flag_note.Text = value

    def add_url(self, i_url: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddURL(CATBSTR iUrl)
                | 
                |     Sets an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set

        :param str i_url:
        :return: None
        :rtype: None
        """
        return self.flag_note.AddURL(i_url)

    def get_nbr_url(self, o_number_of_url: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNbrURL(CATVariant oNumberOfURL)
                | 
                |     Deprecated:
                |         V5-6R2017 This method is replaced by FlagNote.GetNbrURL2

        :param CATVariant o_number_of_url:
        :return: None
        :rtype: None
        """
        return self.flag_note.GetNbrURL(o_number_of_url.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_nbr_url'
        # # vba_code = """
        # # Public Function get_nbr_url(flag_note)
        # #     Dim oNumberOfURL (2)
        # #     flag_note.GetNbrURL oNumberOfURL
        # #     get_nbr_url = oNumberOfURL
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nbr_url2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNbrURL2() As long
                | 
                |     Gets the number of URL.
                | 
                |     Parameters:
                | 
                |         oNumberOfURL
                |             returns param oNumberOfURL.

        :return: int
        :rtype: int
        """
        return self.flag_note.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ModifyURL(CATBSTR iUrl,
                | CATVariant iIndex)
                | 
                |     Modifies an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set. 
                |         iIndex
                |             index of the URL to modify.

        :param str i_url:
        :param CATVariant i_index:
        :return: None
        :rtype: None
        """
        return self.flag_note.ModifyURL(i_url, i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_url'
        # # vba_code = """
        # # Public Function modify_url(flag_note)
        # #     Dim iUrl (2)
        # #     flag_note.ModifyURL iUrl
        # #     modify_url = iUrl
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_url(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveURL(CATVariant iIndex)
                | 
                |     Remove an URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             position of the URL to remove.

        :param CATVariant i_index:
        :return: None
        :rtype: None
        """
        return self.flag_note.RemoveURL(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_url'
        # # vba_code = """
        # # Public Function remove_url(flag_note)
        # #     Dim iIndex (2)
        # #     flag_note.RemoveURL iIndex
        # #     remove_url = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :return: TPSParallelOnScreen
        :rtype: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.flag_note.TPSParallelOnScreen())

    def url(self, i_index: CATVariant) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func URL(CATVariant iIndex) As CATBSTR
                | 
                |     Retrieves URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of URL. 
                |         oUrl
                |             URL

        :param CATVariant i_index:
        :return: str
        :rtype: str
        """
        return self.flag_note.URL(i_index.com_object)

    def __repr__(self):
        return f'FlagNote(name="{ self.name }")'
