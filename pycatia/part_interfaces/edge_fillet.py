#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.part_interfaces.fillet import Fillet


class EdgeFillet(Fillet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 EdgeFillet
                | 
                | Represents the edges-based fillet shape.
                | It is the base object for constant radius edge fillets and variable radius edge
                | fillets.
                | 
                | See also:
                |     ConstRadEdgeFillet, VarRadEdgeFillet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.edge_fillet = com_object

    @property
    def edge_propagation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EdgePropagation() As CatFilletEdgePropagation
                | 
                |     Returns or sets the edge fillet propagation mode. This propagation mode is
                |     used when computing the edges to be filleted.
                | 
                |     Example:
                |         The following example returns in mode the edge fillet propagation mode
                |         of the firstEdgeFillet edge fillet, and then sets it to
                |         CATMinimalFilletEdgePropagation, so that a minimum numbers of edges will be
                |         filleted:
                | 
                |          Set mode = firstEdgeFillet.EdgePropagation
                |          Set firstEdgeFillet.EdgePropagation = CATMinimalFilletEdgePropagation

        :return: int
        :rtype: int
        """

        return self.edge_fillet.EdgePropagation

    @edge_propagation.setter
    def edge_propagation(self, value: int):
        """
        :param int value:
        """

        self.edge_fillet.EdgePropagation = value

    @property
    def edges_to_keep(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EdgesToKeep() As References (Read Only)
                | 
                |     Returns the collection of edges to keep by the edge
                |     fillet.
                | 
                |     Example:
                |         The following example returns in edges the edges to keep of the
                |         constant radius edge fillet firstCstEdgeFillet:
                | 
                |          Set edges = firstCstEdgeFillet.EdgesToKeep

        :return: References
        :rtype: References
        """

        return References(self.edge_fillet.EdgesToKeep)

    def add_edge_to_keep(self, i_edge_to_keep: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddEdgeToKeep(Reference iEdgeToKeep)
                | 
                |     Adds a new edge to keep by the filleting operation. The edge to keep is not
                |     modified by the fillet.
                | 
                |     Parameters:
                | 
                |         iEdgeToKeep
                |             The edge to keep by the filleting operation
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example adds the new edge edge to be kept from filleting by
                |     the constant radius edge fillet firstCstEdgeFillet:
                | 
                |      firstCstEdgeFillet.AddEdgeToKeep(edge)

        :param Reference i_edge_to_keep:
        :return: None
        :rtype: None
        """
        return self.edge_fillet.AddEdgeToKeep(i_edge_to_keep.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_edge_to_keep'
        # # vba_code = """
        # # Public Function add_edge_to_keep(edge_fillet)
        # #     Dim iEdgeToKeep (2)
        # #     edge_fillet.AddEdgeToKeep iEdgeToKeep
        # #     add_edge_to_keep = iEdgeToKeep
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_edge_to_keep(self, i_edge_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawEdgeToKeep(Reference iEdgeToWithdraw)
                | 
                |     Withdraws an edge from those kept by a filleting
                |     operation.
                | 
                |     Parameters:
                | 
                |         iEdgeToWithdraw
                |             The edge to withdraw
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example withdraws the edge edge from those kept from
                |     filleting by the constant radius edge fillet
                |     firstCstEdgeFillet:
                | 
                |      firstCstEdgeFillet.WithdrawEdgeToKeep(edge)

        :param Reference i_edge_to_withdraw:
        :return: None
        :rtype: None
        """
        return self.edge_fillet.WithdrawEdgeToKeep(i_edge_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_edge_to_keep'
        # # vba_code = """
        # # Public Function withdraw_edge_to_keep(edge_fillet)
        # #     Dim iEdgeToWithdraw (2)
        # #     edge_fillet.WithdrawEdgeToKeep iEdgeToWithdraw
        # #     withdraw_edge_to_keep = iEdgeToWithdraw
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'EdgeFillet(name="{self.name}")'
