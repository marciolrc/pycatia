#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Annotation2(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Annotation2
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation2 = com_object

    @property
    def super_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SuperType() As CATBSTR (Read Only)
                | 
                |     Gets the Super Type.
                | 
                |     Parameters:
                | 
                |         oSuperType
                |             The Super Type. The list of SuperType available: "FTA_NonSemantic"
                |             "FTA_Form" "FTA_Dimension" "FTA_Position" "FTA_Datum" "FTA_Orientation"
                |             "FTA_RunOut"

        :return: str
        :rtype: str
        """

        return self.annotation2.SuperType

    @property
    def tps_status(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TPSStatus() As CATBSTR (Read Only)
                | 
                |     Gets the TPS Status.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The Status.

        :return: str
        :rtype: str
        """

        return self.annotation2.TPSStatus

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Gets the Type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The Type. List of types available ordered by SuperType: SuperType = "FTA_NonSemantic" Type = "FTA_Text" Type = "FTA_FlagNote" Type = "FTA_Roughness" Type = "FTA_Weld" Type = "FTA_Noa" Type = "FTA_NonSemanticDatum" Type = "FTA_NonSemanticTarget" Type = "FTA_NonSemanticGDT" Type = "FTA_NonSemanticDimension" SuperType = "FTA_Form" Type = "FTA_Flatness" Type = "FTA_Straightness" Type = "FTA_Circularity" Type = "FTA_Cylindricity" Type = "FTA_ProfileOfAnyLine" Type = "FTA_ProfileOfASurface" Type = "FTA_PatternTruePos" SuperType = "FTA_Dimension" Type = "FTA_LinearDimension" Type = "FTA_AngularDimension" Type = "FTA_SecondLinearDimension" Type = "FTA_ChamferDimension" Type = "FTA_BasicDimension" SuperType = "FTA_Position" Type = "FTA_TruePosition" Type = "FTA_Concentricity" Type = "FTA_Symmetry" Type = "FTA_PositionOfAnyLine" Type = "FTA_PositionOfASurface" SuperType = "FTA_Datum" Type = "FTA_DatumSimple" Type = "FTA_DatumTarget" Type = "FTA_DatumSystem" Type = "FTA_ReferenceFrame" SuperType = "FTA_Orientation" Type = "FTA_Parallelism" Type = "FTA_Perpendicularity" Type = "FTA_Angularity" SuperType = "FTA_RunOut" Type = "FTA_TotalRunOut" Type = "FTA_CircularRunOut"

        :return: str
        :rtype: str
        """

        return self.annotation2.Type

    @property
    def z(self) -> False:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Z(double iZ) (Write Only)
                | 
                |     method get_Z will never be exposed Set the offset of the
                |     annotation
                | 
                |     Parameters:
                | 
                |         iZ
                |             The offset.

        :return: False
        :rtype: False
        """

        return None

    @z.setter
    def z(self, value: False):
        """
        :param False value:
        """

        self.annotation2.Z = value

    def add_leader(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddLeader()
                | 
                |     Add a leader.

        :return: None
        :rtype: None
        """
        return self.annotation2.AddLeader()

    def datum_simple(self) -> 'DatumSimple':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DatumSimple() As DatumSimple
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: DatumSimple
        :rtype: DatumSimple
        """
        import pycatia.cat_tps_interfaces.datum_simple
        return pycatia.cat_tps_interfaces.datum_simple.DatumSimple(self.annotation2.DatumSimple())

    def datum_target(self) -> 'DatumTarget':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DatumTarget() As DatumTarget
                | 
                |     Gets the annotation on the DatumTarget interface.

        :return: DatumTarget
        :rtype: DatumTarget
        """
        import pycatia.cat_tps_interfaces.datum_target
        return pycatia.cat_tps_interfaces.datum_target.DatumTarget(self.annotation2.DatumTarget())

    def default_annotation(self) -> 'DefaultAnnotation':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DefaultAnnotation() As DefaultAnnotation
                | 
                |     Gets the annotation on the DefaultAnnotation interface.

        :return: DefaultAnnotation
        :rtype: DefaultAnnotation
        """
        import pycatia.cat_tps_interfaces.default_annotation
        return pycatia.cat_tps_interfaces.default_annotation.DefaultAnnotation(self.annotation2.DefaultAnnotation())

    def dimension_3d(self) -> 'Dimension3D':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Dimension3D() As Dimension3D
                | 
                |     Gets the 3D Dimension on the 3D Dimension interface.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The 3D Dimension.

        :return: Dimension3D
        :rtype: Dimension3D
        """
        import pycatia.cat_tps_interfaces.dimension_3d
        return pycatia.cat_tps_interfaces.dimension_3d.Dimension3D(self.annotation2.Dimension3D())

    def flag_note(self) -> 'FlagNote':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FlagNote() As FlagNote
                | 
                |     Gets the annotation on the FlagNote interface.
                | 
                |     Parameters:
                | 
                |         oFlagNote
                |             The annotation Flag Note.

        :return: FlagNote
        :rtype: FlagNote
        """
        import pycatia.cat_tps_interfaces.flag_note
        return pycatia.cat_tps_interfaces.flag_note.FlagNote(self.annotation2.FlagNote())

    def get_surfaces(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSurfaces(CATSafeArrayVariant oSafeArray)
                | 
                |     Gets the geometry on which the Annotation is applied to.

        :param tuple o_safe_array:
        :return: None
        :rtype: None
        """
        return self.annotation2.GetSurfaces(o_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_surfaces'
        # # vba_code = """
        # # Public Function get_surfaces(annotation2)
        # #     Dim oSafeArray (2)
        # #     annotation2.GetSurfaces oSafeArray
        # #     get_surfaces = oSafeArray
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_surfaces_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSurfacesCount() As long
                | 
                |     Counts the geometry on which the Annotation is applied to.

        :return: int
        :rtype: int
        """
        return self.annotation2.GetSurfacesCount()

    def has_a_visualization_dimension(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAVisualizationDimension() As boolean
                | 
                |     Checks if the Annotation uses a visualization dimension for its attachment
                |     to the geometry.

        :return: bool
        :rtype: bool
        """
        return self.annotation2.HasAVisualizationDimension()

    def is_a_default_annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsADefaultAnnotation() As boolean
                | 
                |     To know if the Annotation is a Default Annotation.

        :return: bool
        :rtype: bool
        """
        return self.annotation2.IsADefaultAnnotation()

    def modify_visu(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ModifyVisu()
                | 
                |     To refresh the 3D visualization.

        :return: None
        :rtype: None
        """
        return self.annotation2.ModifyVisu()

    def noa(self) -> 'Noa':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Noa() As Noa
                | 
                |     Gets the annotation on the Noa interface.

        :return: Noa
        :rtype: Noa
        """
        import pycatia.cat_tps_interfaces.noa
        return pycatia.cat_tps_interfaces.noa.Noa(self.annotation2.Noa())

    def non_semantic_datum(self) -> 'NonSemanticDatum':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NonSemanticDatum() As NonSemanticDatum
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDatum
        :rtype: NonSemanticDatum
        """
        import pycatia.cat_tps_interfaces.non_semantic_datum
        return pycatia.cat_tps_interfaces.non_semantic_datum.NonSemanticDatum(self.annotation2.NonSemanticDatum())

    def non_semantic_datum_target(self) -> 'NonSemanticDatumTarget':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NonSemanticDatumTarget() As NonSemanticDatumTarget
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDatumTarget
        :rtype: NonSemanticDatumTarget
        """
        import pycatia.cat_tps_interfaces.non_semantic_datum_target
        return pycatia.cat_tps_interfaces.non_semantic_datum_target.NonSemanticDatumTarget(self.annotation2.NonSemanticDatumTarget())

    def non_semantic_dimension(self) -> 'NonSemanticDimension':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NonSemanticDimension() As NonSemanticDimension
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDimension
        :rtype: NonSemanticDimension
        """
        import pycatia.cat_tps_interfaces.non_semantic_dimension
        return pycatia.cat_tps_interfaces.non_semantic_dimension.NonSemanticDimension(self.annotation2.NonSemanticDimension())

    def non_semantic_gdt(self) -> 'NonSemanticGDT':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NonSemanticGDT() As NonSemanticGDT
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticGDT
        :rtype: NonSemanticGDT
        """
        import pycatia.cat_tps_interfaces.non_semantic_gdt
        return pycatia.cat_tps_interfaces.non_semantic_gdt.NonSemanticGDT(self.annotation2.NonSemanticGDT())

    def reference_frame(self) -> 'ReferenceFrame':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ReferenceFrame() As ReferenceFrame
                | 
                |     Gets the annotation on the ReferenceFrame interface.

        :return: ReferenceFrame
        :rtype: ReferenceFrame
        """
        import pycatia.cat_tps_interfaces.reference_frame
        return pycatia.cat_tps_interfaces.reference_frame.ReferenceFrame(self.annotation2.ReferenceFrame())

    def roughness(self) -> 'Roughness':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Roughness() As Roughness
                | 
                |     Gets the annotation on the Roughness interface.

        :return: Roughness
        :rtype: Roughness
        """
        import pycatia.cat_tps_interfaces.roughness
        return pycatia.cat_tps_interfaces.roughness.Roughness(self.annotation2.Roughness())

    def semantic_gdt(self) -> 'SemanticGDT':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SemanticGDT() As SemanticGDT
                | 
                |     Gets the annotation on the DatumSimple interface.

        :return: SemanticGDT
        :rtype: SemanticGDT
        """
        import pycatia.cat_tps_interfaces.semantic_gdt
        return pycatia.cat_tps_interfaces.semantic_gdt.SemanticGDT(self.annotation2.SemanticGDT())

    def set_xy(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetXY(double iX,
                | double iY)
                | 
                |     method GetXY will never be exposed Set TPS coordinates in the
                |     view
                | 
                |     Parameters:
                | 
                |         oX
                |             The X coordinate. 
                |         oY
                |             The Y coordinate.

        :param float i_x:
        :param float i_y:
        :return: None
        :rtype: None
        """
        return self.annotation2.SetXY(i_x, i_y)

    def text(self) -> 'Text':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Text() As Text
                | 
                |     Gets the annotation on the Text interface.
                | 
                |     Parameters:
                | 
                |         oText
                |             The annotation Text.

        :return: Text
        :rtype: Text
        """
        import pycatia.cat_tps_interfaces.text
        return pycatia.cat_tps_interfaces.text.Text(self.annotation2.Text())

    def transfert_to_view(self, i_view: 'TPSView') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub TransfertToView(TPSView iView)
                | 
                |     Move the annotation in another view.
                | 
                |     Parameters:
                | 
                |         iView
                |             The destination view.

        :param TPSView i_view:
        :return: None
        :rtype: None
        """
        return self.annotation2.TransfertToView(i_view.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'transfert_to_view'
        # # vba_code = """
        # # Public Function transfert_to_view(annotation2)
        # #     Dim iView (2)
        # #     annotation2.TransfertToView iView
        # #     transfert_to_view = iView
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def visualization_dimension(self) -> 'Dimension3D':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func VisualizationDimension() As Dimension3D
                | 
                |     Gets the dimension visualization associated with the
                |     annotation.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The visualization Dimension oDim employed by the annotation to
                |             display its link to the geometry.

        :return: Dimension3D
        :rtype: Dimension3D
        """
        import pycatia.cat_tps_interfaces.dimension_3d
        return pycatia.cat_tps_interfaces.dimension_3d.Dimension3D(self.annotation2.VisualizationDimension())

    def weld(self) -> 'Weld':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Weld() As Weld
                | 
                |     Gets the annotation on the Weld interface.

        :return: Weld
        :rtype: Weld
        """
        import pycatia.cat_tps_interfaces.weld
        return pycatia.cat_tps_interfaces.weld.Weld(self.annotation2.Weld())

    def __repr__(self):
        return f'Annotation2(name="{ self.name }")'
