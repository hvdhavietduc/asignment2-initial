from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #program: parsercall_list EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.parsercall_list()))
    
    #parsercall_list: parsercall parsercall_list| parsercall;
    def visitParsercall_list(self,ctx:MT22Parser.Parsercall_listContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.parsercall())
        return self.visit(ctx.parsercall()) + self.visit(ctx.parsercall_list())
    
    #parsercall:( vardecl |funcdecl) ;
    def visitParsercall(self,ctx:MT22Parser.ParsercallContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    #typein: Inttype | Floattype | Stringtype | Booleantype| Autotype ;
    def visitTypein(self,ctx:MT22Parser.TypeinContext):
        if ctx.Inttype():
            return IntegerType()
        elif ctx.Floattype():
            return FloatType()
        elif ctx.Stringtype():
            return StringType()
        elif ctx.Booleantype():
            return BooleanType()
        else:
            return AutoType()
    #funcType: Inttype | Floattype | Stringtype | Booleantype| Voidtype | Autotype | arraytypeof;
    def visitFuncType(self,ctx:MT22Parser.FuncTypeContext):
        if ctx.Inttype():
            return IntegerType()
        elif ctx.Floattype():
            return FloatType()
        elif ctx.Stringtype():
            return StringType()
        elif ctx.Booleantype():
            return BooleanType()
        elif ctx.Voidtype():
            return VoidType()
        elif ctx.Autotype():
            return AutoType()
        else:
            return self.visit(ctx.arraytypeof())
    #typearray: Inttype | Floattype | Stringtype | Booleantype ;
    def visitTypearray(self,ctx:MT22Parser.TypearrayContext):
        if ctx.Inttype():
            return IntegerType()
        elif ctx.Floattype():
            return FloatType()
        elif ctx.Stringtype():
            return StringType()
        else:
            return BooleanType()
    # array_expr : LCB (expression_BT_list|) RCB;
    def visitArray_expr(self,ctx:MT22Parser.Array_exprContext):
        if ctx.expression_BT_list():
            return ArrayLit(self.visit(ctx.expression_BT_list()))
        return ArrayLit([])
    # arraytypeof: Arraytype LSB intlist RSB Ofkey typearray ;
    def visitArraytypeof(self,ctx:MT22Parser.ArraytypeofContext):
        return ArrayType(self.visit(ctx.intlist()), self.visit(ctx.typearray()))
    #intlist: Int COMMA intlist| Int;
    def visitIntlist(self,ctx:MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.Int().getText()]
        return [ctx.Int().getText()] + self.visit(ctx.intlist())
    #idlist: Identifiers COMMA idlist |Identifiers ;
    def visitIdlist(self,ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() ==1:
            return [Id(ctx.Identifiers().getText())]
        return [Id(ctx.Identifiers().getText())] + self.visit(ctx.idlist())
    
    #expression_list : expression_BT| expression_BT COMMA expression_list;
    def visitExpression_list(self,ctx:MT22Parser.Expression_listContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.expression_BT())]
        return [self.visit(ctx.expression_BT())]+self.visit(ctx.expression_list())  

    # vardecl: idlist COLON (typein| arraytypeof) SEMI | varinit  ;   
    def visitVardecl(self,ctx:MT22Parser.VardeclContext):
        if ctx.getChildCount()==1:
            listvar = self.visit(ctx.varinit())
            lenlistvar = len(listvar)
            j=lenlistvar-2
            for x in listvar[:1 if lenlistvar==3 else round((lenlistvar-2)/2)]:
                temp = x[1]
                x[1] = listvar[j][1]
                listvar[j][1] = temp
                j=j-1
            res = []
            for x in listvar[:lenlistvar-1]:
                res = res + [VarDecl(x[0],listvar[lenlistvar-1], x[1])]
            return res
        listID = self.visit(ctx.idlist())
        result = []
        typein = self.visit(ctx.typein()) if ctx.typein() else self.visit(ctx.arraytypeof());
        for x in listID:

            result = result + [VarDecl(x.name, typein)]
        return result

    # varinit: Identifiers (COMMA re_vardecl | COLON (typein|arraytypeof) ASS) (expression_BT) SEMI;
    def visitVarinit(self,ctx:MT22Parser.VarinitContext):
        if ctx.COLON():
            typein = self.visit(ctx.typein()) if ctx.typein() else self.visit(ctx.arraytypeof())
            return [[ctx.Identifiers().getText(),self.visit(ctx.expression_BT())],typein]
        return [[ctx.Identifiers().getText(),self.visit(ctx.expression_BT())]] + self.visit(ctx.re_vardecl())

    # re_vardecl: Identifiers (COMMA re_vardecl | COLON (typein| arraytypeof) ASS ) (expression_BT) COMMA;
    def visitRe_vardecl(self,ctx:MT22Parser.Re_vardeclContext):
        if ctx.COLON():
            typein = self.visit(ctx.typein()) if ctx.typein() else self.visit(ctx.arraytypeof())
            return [[ctx.Identifiers().getText(),self.visit(ctx.expression_BT())],typein]
        return [[ctx.Identifiers().getText(),self.visit(ctx.expression_BT())]] + self.visit(ctx.re_vardecl())

    # parameters: Inheritkey? Outkey? Identifiers COLON (typein|arraytypeof) ; // -------------------------------------------------------Parameters----------------------
    def visitParameters(self,ctx:MT22Parser.ParametersContext):
        checkInheritkey = False
        checkOutkey = False
        if ctx.Inheritkey():
            checkInheritkey = True
        if ctx.Outkey():
            checkOutkey = True
        typein = self.visit(ctx.typein()) if ctx.typein() else self.visit(ctx.arraytypeof())
        return ParamDecl(ctx.Identifiers().getText(),typein ,checkOutkey,checkInheritkey)

    # parameters_list: parameters COMMA parameters_list| parameters;
    def visitParameters_list(self,ctx:MT22Parser.Parameters_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameters())]
        return [self.visit(ctx.parameters())] + self.visit(ctx.parameters_list())

    # //----------------------------------------------------------------------------------------------------------------Khai bao function------------
    # funcdecl: Identifiers COLON Functionkey funcType LB  parameters_list?  RB  (Inheritkey Identifiers)? blockstatement ;
    def visitFuncdecl(self,ctx:MT22Parser.FuncdeclContext):
        list_param = self.visit(ctx.parameters_list()) if ctx.parameters_list() else []
        id2 =  ctx.Identifiers(1).getText() if ctx.Inheritkey() else None
        return [FuncDecl(ctx.Identifiers(0).getText(),self.visit(ctx.funcType()), list_param, id2 , self.visit(ctx.blockstatement()))]
    
    # //----------------------------------------------------------------------------------------------------------------Index Array----------
    # indexopr: Identifiers LSB expression_list RSB;
    def visitIndexopr(self, ctx:MT22Parser.IndexoprContext):
        return ArrayCell(ctx.Identifiers().getText(), self.visit(ctx.expression_list()))
    # //----------------------------------------------------------------------------------------------------------------Goi function----------
    # callfunc: special_function| Identifiers  LB expression_list?  RB ;
    def visitCallfunc(self,ctx:MT22Parser.CallfuncContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.special_function())
        exprlist= self.visit(ctx.expression_list()) if ctx.expression_list() else []
        return FuncCall(ctx.Identifiers().getText(),exprlist )
    
    
    # expression_BT: stringoprExpr  ;
    def visitExpression_BT(self,ctx:MT22Parser.Expression_BTContext):
        return self.visit(ctx.stringoprExpr())
    
    #stringoprExpr: equalityExpr (Stringopr) equalityExpr| equalityExpr;
    def visitStringoprExpr(self,ctx:MT22Parser.StringoprExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpr(0))
        return BinExpr(ctx.Stringopr().getText(), self.visit(ctx.equalityExpr(0)), self.visit(ctx.equalityExpr(1)))
    # equalityExpr
    # :  logicalExpr(EQUAL | NOT_EQUAL|GT | LT | GTE | LTE) logicalExpr
    # | logicalExpr
    # ;
    def visitEqualityExpr(self,ctx:MT22Parser.EqualityExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalExpr(0))
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
        elif ctx.NOT_EQUAL():
            return BinExpr(ctx.NOT_EQUAL().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
        elif ctx.GT():
            return BinExpr(ctx.GT().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
        elif ctx.LT():
            return BinExpr(ctx.LT().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
        elif ctx.GTE():
            return BinExpr(ctx.GTE().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
        elif ctx.LTE():
            return BinExpr(ctx.LTE().getText(), self.visit(ctx.logicalExpr(0)),self.visit(ctx.logicalExpr(1)))
    # logicalExpr
    # :  logicalExpr(LOGICAL_AND|LOGICAL_OR) addExpr
    # | addExpr
    # ;
    def visitLogicalExpr(self,ctx:MT22Parser.LogicalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.addExpr())
        if ctx.LOGICAL_AND():
            return BinExpr(ctx.LOGICAL_AND().getText(), self.visit(ctx.logicalExpr()),self.visit(ctx.addExpr()))
        else:
            return BinExpr(ctx.LOGICAL_OR().getText(), self.visit(ctx.logicalExpr()),self.visit(ctx.addExpr()))
    # addExpr
    # :   addExpr(PLUS | MINUS) multExpr 
    # | multExpr
    # ;
    def visitAddExpr(self,ctx:MT22Parser.AddExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multExpr())
        if ctx.PLUS():
            return BinExpr(ctx.PLUS().getText(), self.visit(ctx.addExpr()),self.visit(ctx.multExpr()))
        else:
            return BinExpr(ctx.MINUS().getText(), self.visit(ctx.addExpr()),self.visit(ctx.multExpr()))
    # multExpr
    # :   multExpr(MULT| DIV | MOD) unaryExpr 
    # | unaryExpr
    # ;
    def visitMultExpr(self,ctx:MT22Parser.MultExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpr())
        if ctx.MULT():
            return BinExpr(ctx.MULT().getText(), self.visit(ctx.multExpr()),self.visit(ctx.unaryExpr()))
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.multExpr()),self.visit(ctx.unaryExpr()))
        else:
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.multExpr()),self.visit(ctx.unaryExpr()))
    # unaryExpr
    # : MINUS unaryExpr
    # | NOT unaryExpr
    # | atom
    # ;
    def visitUnaryExpr(self,ctx:MT22Parser.UnaryExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.atom())
        if ctx.MINUS():
            return UnExpr(ctx.MINUS().getText(), self.visit(ctx.unaryExpr()))
        else:
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.unaryExpr()))
    
    #   
    # : Identifiers
    # | Identifiers LSB expression_BT RSB
    # | FLOAT
    # | indexopr
    # | Int
    # | callfunc 
    # | booleann
    # | String
    # | LB expression_BT RB
    # | array_expr
    # ;
    def visitAtom(self,ctx:MT22Parser.AtomContext):
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.Identifiers().getText(), [self.visit(ctx.expression_BT())])
        if ctx.FLOAT():
            floatval = ctx.FLOAT().getText()
            if floatval[0]=='.' and (floatval[1]=='e' or floatval[1]=='E'):
                return FloatLit(0.0)
            return FloatLit(float(ctx.FLOAT().getText()))
        elif ctx.indexopr():
            return self.visit(ctx.indexopr())
        elif ctx.Int():
            return IntegerLit(int(ctx.Int().getText()))
        elif ctx.callfunc():
            return self.visit(ctx.callfunc())
        elif ctx.booleann() :
            return self.visit(ctx.booleann())
        elif ctx.String():
            return StringLit(str(ctx.String().getText()))
        elif ctx.expression_BT():  
             return self.visit(ctx.expression_BT())
        elif ctx.Identifiers():
            return Id(ctx.Identifiers().getText())
        else:
            return self.visit(ctx.array_expr())
    
    #booleann: Trueboolean|Falseboolean;
    def visitBooleann(self,ctx:MT22Parser.BooleannContext):
        return BooleanLit(True) if ctx.Trueboolean() else BooleanLit(False)
    
    #expression_BT_list: expression_BT| expression_BT COMMA expression_BT_list;
    def visitExpression_BT_list(self,ctx:MT22Parser.Expression_BT_listContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.expression_BT())]
        return [self.visit(ctx.expression_BT())]+self.visit(ctx.expression_BT_list())
    #allstatement: assignment
    #             |if_statement
    #             |for_statement
    #             |while_statements
    #             |do_while_statements
    #             |break_stt
    #             |continue_stt
    #             |retunr_stt
    #             |call_stt
    #             |blockstatement
    #             ;
    def visitAllstatement(self,ctx:MT22Parser.AllstatementContext):
        return self.visitChildren(ctx)


    # //--------------------------------------------------------------------------------------------------Gán-------------------
    # assignment: (Identifiers |indexopr) ASS (expression_BT) SEMI;
    def visitAssignment(self,ctx:MT22Parser.AssignmentContext):
        lhs = Id(ctx.Identifiers().getText()) if ctx.Identifiers() else self.visit(ctx.indexopr())
        return AssignStmt(lhs, self.visit(ctx.expression_BT()))

    # //--------------------------------------------------------------------------------------------------If else------------
    # if_statement: Ifkey LB expression_BT RB  allstatement (Else allstatement)?;
    def visitIf_statement(self,ctx:MT22Parser.If_statementContext):
        elsestmt = self.visit(ctx.allstatement(1)) if ctx.Else() else None
        return IfStmt(self.visit(ctx.expression_BT()), self.visit(ctx.allstatement(0)), elsestmt)

    # //---------------------------------------------------------------------------------------------------For-------------
    # for_statement: Forkey LB  assignment_offor COMMA expression_BT COMMA expression_BT  RB  allstatement;
    def visitFor_statement(self,ctx:MT22Parser.For_statementContext):
        return ForStmt(self.visit(ctx.assignment_offor()), self.visit(ctx.expression_BT(0)),self.visit(ctx.expression_BT(1)), self.visit(ctx.allstatement()) )
    
    
    # assignment_offor:  (Identifiers |indexopr) ASS expression_BT;
    def visitAssignment_offor(self,ctx:MT22Parser.Assignment_offorContext):
        assoffor = Id(ctx.Identifiers().getText()) if ctx.Identifiers() else self.visit(ctx.indexopr()) 
        return AssignStmt(assoffor, self.visit(ctx.expression_BT()))

    # //--------------------------------------------------------------------------------------------------while statement---------
    # while_statements: Whilekey  LB  expression_BT  RB  allstatement;
    def visitWhile_statements(self,ctx:MT22Parser.While_statementsContext):
        return WhileStmt(self.visit(ctx.expression_BT()), self.visit(ctx.allstatement()))

    # //--------------------------------------------------------------------------------------------------do-while statement---------
    # do_while_statements: Dokey blockstatement Whilekey  LB expression_BT  RB  SEMI;
    def visitDo_while_statements(self,ctx:MT22Parser.Do_while_statementsContext):
        return DoWhileStmt(self.visit(ctx.expression_BT()), self.visit(ctx.blockstatement()))

    # //--------------------------------------------------------------------------------------------------break statement---------
    # break_stt: Breakkey SEMI;
    def visitBreak_stt(self,ctx:MT22Parser.Break_sttContext):
        return BreakStmt()
    
    
    # //--------------------------------------------------------------------------------------------------continue statement---------
    # continue_stt: Continuekey SEMI;
    def visitContinue_stt(self,ctx:MT22Parser.Continue_sttContext):
        return ContinueStmt()
    # //--------------------------------------------------------------------------------------------------return statement---------
    # retunr_stt: Returnkey (expression_BT)? SEMI;
    def visitRetunr_stt(self,ctx:MT22Parser.Retunr_sttContext):
        returnstt= self.visit(ctx.expression_BT()) if ctx.expression_BT() else None
        return ReturnStmt(returnstt)
   
    # //--------------------------------------------------------------------------------------------------call statement---------
    # call_stt: callfunc SEMI | Identifiers  LB  expression_BT_list?  RB  SEMI;
    def visitCall_stt(self,ctx:MT22Parser.Call_sttContext):
        if ctx.callfunc():
            func = self.visit(ctx.callfunc())
            name = func.name
            args = func.args
            return CallStmt(name,args )
        callstt = self.visit(ctx.expression_BT_list()) if ctx.expression_BT_list() else []
        return CallStmt(ctx.Identifiers().getText(), callstt)
    # //--------------------------------------------------------------------------------------------------Block statement---------
    # blockstatement: 
    #     LCB
    #     block_allstatement?
    #     RCB
    #     ;

    def visitBlockstatement(self,ctx:MT22Parser.BlockstatementContext):
        return BlockStmt(self.visit(ctx.block_allstatement()) if ctx.block_allstatement() else [])

    # block_allstatement: blockstt block_allstatement| blockstt;
    def visitBlock_allstatement(self,ctx:MT22Parser.Block_allstatementContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.blockstt())
        return self.visit(ctx.blockstt()) + self.visit(ctx.block_allstatement())
    # blockstt: 
    #         assignment
    #         |if_statement
    #         |for_statement
    #         |while_statements
    #         |do_while_statements
    #         |break_stt
    #         |continue_stt
    #         |retunr_stt
    #         |call_stt
    #         |vardecl
    #         |allstatement
    # ;
    def visitBlockstt(self,ctx:MT22Parser.BlocksttContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())  
        return [self.visitChildren(ctx)]

    # //----------------------------------------------------------------Special function------------------

    # special_function:
    #     readInt_function
    #     | printInteger_function
    #     | readFloat_function
    #     | writeFloat_function
    #     | readBoolean_function
    #     | printBoolean_function
    #     | readString_function
    #     | printString_function
    #     | super_function
    #     | preventDefault
    #     ;
    def visitSpecial_function(self,ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)
    # readInt_function: 'readInteger' LB RB;
    def visitReadInt_function(self,ctx:MT22Parser.ReadInt_functionContext):
        return FuncCall("readInteger", [])
    

    # printInteger_function: 'printInteger' LB expression_BT RB;
    def visitPrintInteger_function(self,ctx:MT22Parser.PrintInteger_functionContext):
        return FuncCall("printInteger", [self.visit(ctx.expression_BT())])
    

    # readFloat_function: 'readFloat' LB RB;
    def visitReadFloat_function(self,ctx:MT22Parser.ReadFloat_functionContext):
        return FuncCall("readFloat", [])
    

    # writeFloat_function: 'writeFloat' LB expression_BT RB;
    def visitWriteFloat_function(self,ctx:MT22Parser.WriteFloat_functionContext):
        return FuncCall("writeFloat", [self.visit(ctx.expression_BT())])
    

    # readBoolean_function: 'readBoolean' LB RB;
    def visitReadBoolean_function(self,ctx:MT22Parser.ReadBoolean_functionContext):
        return FuncCall("readBoolean", [])
    

    # printBoolean_function: 'printBoolean' LB expression_BT RB;
    def visitPrintBoolean_function(self,ctx:MT22Parser.PrintBoolean_functionContext):
        return FuncCall("printBoolean", [self.visit(ctx.expression_BT())])
    

    # readString_function: 'readString' LB RB;
    def visitReadString_function(self,ctx:MT22Parser.ReadString_functionContext):
        return FuncCall("readString", [])
    

    # printString_function: 'printString' LB expression_BT RB;
    def visitPrintString_function(self,ctx:MT22Parser.PrintString_functionContext):
        return FuncCall("printString", [self.visit(ctx.expression_BT())])
    

    # super_function: 'super' LB expression_BT_list RB;'
    def visitSuper_function(self,ctx:MT22Parser.Super_functionContext):
        return FuncCall("super", self.visit(ctx.expression_BT_list()))
    

    # preventDefault: 'preventDefault' LB RB;
    def visitPreventDefault(self,ctx:MT22Parser.PreventDefaultContext):
        return FuncCall("preventDefault", [])
    


   

