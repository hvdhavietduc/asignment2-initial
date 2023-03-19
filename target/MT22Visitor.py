# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parsercall_list.
    def visitParsercall_list(self, ctx:MT22Parser.Parsercall_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parsercall.
    def visitParsercall(self, ctx:MT22Parser.ParsercallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcType.
    def visitFuncType(self, ctx:MT22Parser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_expr.
    def visitArray_expr(self, ctx:MT22Parser.Array_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytypeof.
    def visitArraytypeof(self, ctx:MT22Parser.ArraytypeofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varinit.
    def visitVarinit(self, ctx:MT22Parser.VarinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#re_vardecl.
    def visitRe_vardecl(self, ctx:MT22Parser.Re_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters.
    def visitParameters(self, ctx:MT22Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters_list.
    def visitParameters_list(self, ctx:MT22Parser.Parameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexopr.
    def visitIndexopr(self, ctx:MT22Parser.IndexoprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callfunc.
    def visitCallfunc(self, ctx:MT22Parser.CallfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_BT.
    def visitExpression_BT(self, ctx:MT22Parser.Expression_BTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringoprExpr.
    def visitStringoprExpr(self, ctx:MT22Parser.StringoprExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#equalityExpr.
    def visitEqualityExpr(self, ctx:MT22Parser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpr.
    def visitLogicalExpr(self, ctx:MT22Parser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addExpr.
    def visitAddExpr(self, ctx:MT22Parser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multExpr.
    def visitMultExpr(self, ctx:MT22Parser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unaryExpr.
    def visitUnaryExpr(self, ctx:MT22Parser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atom.
    def visitAtom(self, ctx:MT22Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_BT_list.
    def visitExpression_BT_list(self, ctx:MT22Parser.Expression_BT_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#allstatement.
    def visitAllstatement(self, ctx:MT22Parser.AllstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment.
    def visitAssignment(self, ctx:MT22Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_offor.
    def visitAssignment_offor(self, ctx:MT22Parser.Assignment_offorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statements.
    def visitWhile_statements(self, ctx:MT22Parser.While_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_statements.
    def visitDo_while_statements(self, ctx:MT22Parser.Do_while_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stt.
    def visitBreak_stt(self, ctx:MT22Parser.Break_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stt.
    def visitContinue_stt(self, ctx:MT22Parser.Continue_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#retunr_stt.
    def visitRetunr_stt(self, ctx:MT22Parser.Retunr_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stt.
    def visitCall_stt(self, ctx:MT22Parser.Call_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstatement.
    def visitBlockstatement(self, ctx:MT22Parser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_allstatement.
    def visitBlock_allstatement(self, ctx:MT22Parser.Block_allstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstt.
    def visitBlockstt(self, ctx:MT22Parser.BlocksttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_function.
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInt_function.
    def visitReadInt_function(self, ctx:MT22Parser.ReadInt_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInteger_function.
    def visitPrintInteger_function(self, ctx:MT22Parser.PrintInteger_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat_function.
    def visitReadFloat_function(self, ctx:MT22Parser.ReadFloat_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat_function.
    def visitWriteFloat_function(self, ctx:MT22Parser.WriteFloat_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoolean_function.
    def visitReadBoolean_function(self, ctx:MT22Parser.ReadBoolean_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoolean_function.
    def visitPrintBoolean_function(self, ctx:MT22Parser.PrintBoolean_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString_function.
    def visitReadString_function(self, ctx:MT22Parser.ReadString_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString_function.
    def visitPrintString_function(self, ctx:MT22Parser.PrintString_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_function.
    def visitSuper_function(self, ctx:MT22Parser.Super_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typein.
    def visitTypein(self, ctx:MT22Parser.TypeinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleann.
    def visitBooleann(self, ctx:MT22Parser.BooleannContext):
        return self.visitChildren(ctx)



del MT22Parser