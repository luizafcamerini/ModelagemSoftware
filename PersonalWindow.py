from ui_PersonalWindow import Ui_PersonalWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from usuario import Usuario
from banco import Banco

class PersonalWindow(QWidget, Banco):
    matricula = None
    nome = ""

    # Signals
    logout = Signal()
    cad_usuario = Signal()
    conf_treino = Signal()
    cria_programa = Signal(list)
    alt_treino = Signal()
    cad_exercicio = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PersonalWindow()
        self.ui.setupUi(self)
    
        bd = Banco.get_instance().get_database()
        clientes = bd["clientes"]
        self.exercicios_col = bd["exercicios"]

        # Connects
        self.ui.logout_button.clicked.connect(self.logoutClicked)
        self.ui.programa_button.clicked.connect(self.criarProgramaClicked)
        self.ui.configurar_treino_button.clicked.connect(self.configurarTreinoClicked)
        self.ui.cad_exercicio_button.clicked.connect(self.cadastraExercicioClicked)

    # Slots
    @Slot()
    def logoutClicked(self):
        self.logout.emit()

    @Slot()
    def cadastrarUsuarioClicked(self):
        self.cad_usuario.emit()
    
    @Slot()
    def configurarTreinoClicked(self):
        self.conf_treino.emit()

    @Slot()
    def criarProgramaClicked(self):
        exercicios = list(self.exercicios_col.find())
        self.cria_programa.emit(exercicios)
    
    @Slot()
    def alterarTreinoClicked(self):
        self.alt_treino.emit()
    
    @Slot()
    def cadastraExercicioClicked(self):
        exercicios = list(self.exercicios_col.find())
        self.cad_exercicio.emit(exercicios)


    # Publicos
    def updateSolicitacoesPendentes(self, usuarios):
        
        pass

    def updateSolicitacoesRespondidas(self, usuarios):
        pass

    def setCurrentUser(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

 