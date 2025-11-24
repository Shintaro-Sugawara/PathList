# --------------------------------------
# 先行ロード対象
# --------------------------------------
import locale           # 現在の（言語と地域）の取得用
import sys              # コマンドライン引数の取得
import win32com.client  # Windowsショートカット（.lnk）のリンク先取得
import os               # ファイル・フォルダ操作（パス操作、存在確認、リスト取得など）
import ctypes           # Windows API呼び出し（高ＰＤＩ対応）
import wx               # GUI作成（ダイアログやコントロール表示）
import datetime         # 日付・時刻の取得（出力ファイルのタイムスタンプなど）
# import threading        # マルチスレッド用（ライブラリのバックグランドでのインポート）

# 遅延ロード対象
# import openpyxl         # Excel出力用    【Listのみ使用】Pro版

# --------------------------------------
# マルチスレッド（ライブラリの遅延ロード）
# --------------------------------------
# def preload_all_async():
#    for name in ["subprocess"]:
#        threading.Thread(
#            target=lambda n=name: globals().__setitem__(n, __import__(n)),
#            daemon=True
#        ).start()

# --------------------------------------
# ロケール（言語と地域）の取得
# --------------------------------------
current_locale = locale.getdefaultlocale()

# 言語の取得（取得不能時は英語判定）
language_code = current_locale[0] if current_locale else "en"

# --------------------------------------
# 辞書（多言語対応用）
# --------------------------------------
LABELS = {
    "ja": {
        "APP_TITLE": "Path List",
        "LABEL_ARGS_FALSE": "このダイアログにフォルダをドロップしてください。",
        "LABEL_ARGS_TRUE": "フォルダパス取得済み。",
        "LABEL_INTRO": "以下で選択した内容で、デスクトップに一覧を作成します。",
        "LABEL_TARGET_TYPE": "どちらの一覧を作成しますか？",
        "LABEL_FILE": "ファイル",
        "LABEL_FOLDER": "フォルダ",
        "LABEL_EXCLUDE": "取得しない",
        "LABEL_INCLUDE": "取得する",
        "LABEL_SUBFOLDER": "サブフォルダ内の情報も取得しますか？",
        "BTN_OK": "OK",
        "BTN_CANCEL": "キャンセル",
        "MSG_COMPLETE": "デスクトップにファイルを作成しました。",
        "BTN_OPEN": "開く",
        "BTN_CLOSE": "終了",
        "MSG_REDROP": "フォルダパスを再取得しました。",
        "MSG_OPEN_ERROR": "ファイルを開けませんでした。",
        "MSG_ERROR": "エラー"
    },

    "de": {
        "APP_TITLE": "Path List",
        "LABEL_ARGS_FALSE": "Bitte ziehen Sie den Ordner auf diesen Dialog.",
        "LABEL_ARGS_TRUE": "Der Ordnerpfad wurde bereits ermittelt.",
        "LABEL_INTRO": "Eine Liste wird auf Ihrem Desktop erstellt.",
        "LABEL_TARGET_TYPE": "Welche Liste möchten Sie erstellen?",
        "LABEL_FILE": "Datei",
        "LABEL_FOLDER": "Ordner",
        "LABEL_EXCLUDE": "Ausschließen",
        "LABEL_INCLUDE": "Einbeziehen",
        "LABEL_SUBFOLDER": "Möchten Sie Unterordner einbeziehen?",
        "BTN_OK": "OK",
        "BTN_CANCEL": "Abbrechen",
        "MSG_COMPLETE": "Die Datei wurde auf dem Desktop erstellt.",
        "BTN_OPEN": "Öffnen && Beenden",
        "BTN_CLOSE": "Nur schließen",
        "MSG_REDROP": "Der Ordnerpfad wurde erneut abgerufen.",
        "MSG_OPEN_ERROR": "Die Datei konnte nicht geöffnet werden.",
        "MSG_ERROR": "Fehler"
    },

    "en": {
        "APP_TITLE": "Path List",
        "LABEL_ARGS_FALSE": "Please drop the folder onto this dialog.",
        "LABEL_ARGS_TRUE": "The folder path has been retrieved.",
        "LABEL_INTRO": "A list will be created on the desktop.",
        "LABEL_TARGET_TYPE": "Which list would you like to create?",
        "LABEL_FILE": "File",
        "LABEL_FOLDER": "Folder",
        "LABEL_EXCLUDE": "Exclude",
        "LABEL_INCLUDE": "Include",
        "LABEL_SUBFOLDER": "Do you want to include subfolders?",
        "BTN_OK": "OK",
        "BTN_CANCEL": "Cancel",
        "MSG_COMPLETE": "The file has been created on the desktop.",
        "BTN_OPEN": "Open && Exit",
        "BTN_CLOSE": "Exit Only",
        "MSG_REDROP": "The folder path has been retrieved again.",
        "MSG_OPEN_ERROR": "Could not open the file.",
        "MSG_ERROR": "Error"
    }
}

# --------------------------------------
# 定数定義（多言語対応用）
# --------------------------------------
# 使用言語の選択（日本語・ドイツ語以外は英語）
if language_code.startswith("ja"):
    lang = "ja"
elif language_code.startswith("de"):
    lang = "de"
else:
    lang = "en"

L = LABELS[lang]

# ダイアログ・UIメッセージ
APP_TITLE = L["APP_TITLE"]
LABEL_ARGS = L["LABEL_ARGS_FALSE"]
LABEL_INTRO = L["LABEL_INTRO"]
LABEL_TARGET_TYPE = L["LABEL_TARGET_TYPE"]
LABEL_FILE = L["LABEL_FILE"]
LABEL_FOLDER = L["LABEL_FOLDER"]
LABEL_EXCLUDE = L["LABEL_EXCLUDE"]
LABEL_INCLUDE = L["LABEL_INCLUDE"]
LABEL_SUBFOLDER = L["LABEL_SUBFOLDER"]
BTN_OK = L["BTN_OK"]
BTN_CANCEL = L["BTN_CANCEL"]
MSG_REDROP = L["MSG_REDROP"]

# 完了ダイアログ
MSG_COMPLETE = L["MSG_COMPLETE"]
BTN_OPEN = L["BTN_OPEN"]
BTN_CLOSE = L["BTN_CLOSE"]
MSG_OPEN_ERROR = L["MSG_OPEN_ERROR"]
MSG_ERROR = L["MSG_ERROR"]

# --------------------------------------
# 変数定義（常用のみ）
# --------------------------------------
valid_args = []             # コマンドライン引数リスト
target_type = 'file'        # 他：folder
include_subfolders = True

# --------------------------------------
# 高DPI対応（Windows 10/11専用）
# --------------------------------------
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

# --------------------------------------
# .lnk のリンク先を取得（pywin32 使用）
# --------------------------------------
def resolve_shortcut(path):
    if path.lower().endswith(".lnk") and os.path.isfile(path):
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(path)
            return shortcut.TargetPath
        except Exception:
            return None
    return path

# --------------------------------------
# ドロップフォルダを取得（.lnkの場合はリンク先）
# ※ファイルの場合は親ディレクトリを返す
# ※重複するパスは変数に追加しない
# --------------------------------------
def validate_args(args):
    valid = []
    for p in args:
        resolved = resolve_shortcut(p)
        if resolved:
            if os.path.isdir(resolved):
                if resolved not in valid:
                    valid.append(resolved)
            elif os.path.isfile(resolved):
                dir_path = os.path.dirname(resolved)
                if dir_path not in valid:
                    valid.append(dir_path)
    return valid

# --------------------------------------
# ファイル・フォルダ収集（os.scandir使用）
# --------------------------------------
def collect_paths(paths, target_type, include_subfolders):
    results = []

    # 指定されたパスを再帰的に走査する関数
    def scan_directory(base_abs):
        try:
            with os.scandir(base_abs) as it:
                for entry in it:
                    # ファイル判定（シンボリックリンクは除外）
                    if target_type == 'file' and entry.is_file(follow_symlinks=False):
                        results.append(entry.path)

                    # フォルダ判定（シンボリックリンクは除外）
                    elif entry.is_dir(follow_symlinks=False):
                        if target_type == 'folder':
                            results.append(entry.path)

                        # サブフォルダも含める場合は再帰的に走査
                        if include_subfolders:
                            scan_directory(entry.path)
        except (PermissionError, FileNotFoundError):
            # アクセス権がない、または削除済みのフォルダはスキップ
            pass

    for base_path in paths:
        base_abs = os.path.abspath(base_path)
        if os.path.isdir(base_abs):
            scan_directory(base_abs)

    return results

# --------------------------------------
# ドロップ処理クラス（フォルダ／ファイル受け取り用）
# --------------------------------------
class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def OnDropFiles(self, x, y, filenames):
        # ドロップされたファイル／フォルダを検証してグローバル状態に反映
        global valid_args, LABEL_ARGS

        # 直前までの状態を記録
        was_valid = bool(valid_args)

        # 新しいドロップを検証
        valid_args = validate_args(filenames)

        # LABEL_ARGS を更新
        if valid_args:
            LABEL_ARGS = L["LABEL_ARGS_TRUE"]
        else:
            LABEL_ARGS = L["LABEL_ARGS_FALSE"]

        # ラベル再設定
        self.parent.lbl_intro.SetLabel(LABEL_ARGS)

        # 色・フォント切替
        if not valid_args:
            self.parent.lbl_intro.SetFont(self.parent.font.Bold())
            self.parent.lbl_intro.SetForegroundColour(wx.Colour(255, 0, 0))  # 赤
        else:
            self.parent.lbl_intro.SetFont(self.parent.font.Bold())
            self.parent.lbl_intro.SetForegroundColour(wx.Colour(0, 0, 255))  # 青
        self.parent.main_sizer.Layout()
        self.parent.lbl_intro.CenterOnParent(wx.HORIZONTAL)

        # ボタン有効／無効切替
        self.parent.btn_ok.Enable(bool(valid_args))

        # 「以前も有効だった → 今回も有効」なら再取得のメッセージ表示
        if was_valid and valid_args:
            wx.MessageBox(MSG_REDROP, APP_TITLE, wx.OK | wx.ICON_INFORMATION)

        return True

# --------------------------------------
# メインダイアログのＵＩ作成
# --------------------------------------
class MainDialog(wx.Dialog):

    # --------------------------------------
    # パスの一覧（フリー版）用ＵＩ
    # --------------------------------------
    def __init__(self, parent, font=None):
        super().__init__(parent, title=APP_TITLE, style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        base_margin = 10
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # フォント受け取りと適用（Noneならシステムデフォルトを取得）
        if font is None:
            font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
            font.SetPointSize(font.GetPointSize() + 1)  # 少し大きくする（任意）

        self.font = font
        self.SetFont(self.font)

        # ドラッグ＆ドロップ状況
        self.main_sizer.AddSpacer(12)
        self.lbl_intro = wx.StaticText(self, label=LABEL_ARGS)

        if not valid_args:
            self.lbl_intro.SetFont(self.font.Bold())
            self.lbl_intro.SetForegroundColour(wx.Colour(255, 0, 0))  # 赤
        else:
            self.lbl_intro.SetFont(self.font.Bold())
            self.lbl_intro.SetForegroundColour(wx.Colour(0, 0, 255))  # 青

        self.main_sizer.Add(self.lbl_intro, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, base_margin)
        self.main_sizer.AddSpacer(12)

        # カスタム区切り線（薄いグレー）  ※ wx.Panelを「線のような矩形」として利用
        line_custom = wx.Panel(self, size=(-1, 1))
        line_custom.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.main_sizer.Add(line_custom, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, base_margin)
        self.main_sizer.AddSpacer(12)

        # イントロラベル
        lbl_intro = wx.StaticText(self, label=LABEL_INTRO)
        lbl_intro.SetFont(self.font)
        self.main_sizer.Add(lbl_intro, 0, wx.LEFT | wx.RIGHT, base_margin)
        self.main_sizer.AddSpacer(5)

        self.sizer_pathlist = wx.BoxSizer(wx.VERTICAL)
        # ファイル/フォルダ選択ラベル
        lbl_target_type = wx.StaticText(self, label=LABEL_TARGET_TYPE)
        lbl_target_type.SetFont(self.font)
        self.sizer_pathlist.Add(lbl_target_type, 0, wx.LEFT, base_margin)
        self.sizer_pathlist.AddSpacer(2)

        # ファイル/フォルダ選択ラジオボタン
        self.rb_file = wx.RadioButton(self, label=LABEL_FILE, style=wx.RB_GROUP)
        self.rb_folder = wx.RadioButton(self, label=LABEL_FOLDER)
        self.rb_file.SetValue(True)
        file_folder_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_folder_sizer.Add(self.rb_file, 0, wx.RIGHT, 5)
        file_folder_sizer.Add(self.rb_folder, 0)
        self.sizer_pathlist.Add(file_folder_sizer, 0, wx.LEFT, base_margin)
        self.sizer_pathlist.AddSpacer(12)

        # サブフォルダラベル
        lbl_sub = wx.StaticText(self, label=LABEL_SUBFOLDER)
        lbl_sub.SetFont(self.font)
        self.sizer_pathlist.Add(lbl_sub, 0, wx.LEFT, base_margin)
        self.sizer_pathlist.AddSpacer(2)

        # サブフォルダラジオボタン
        self.rb_exclude = wx.RadioButton(self, label=LABEL_EXCLUDE, style=wx.RB_GROUP)
        self.rb_include = wx.RadioButton(self, label=LABEL_INCLUDE)
        self.rb_include.SetValue(True)
        include_sizer = wx.BoxSizer(wx.HORIZONTAL)
        include_sizer.Add(self.rb_exclude, 0, wx.RIGHT, 5)
        include_sizer.Add(self.rb_include, 0)
        self.sizer_pathlist.Add(include_sizer, 0, wx.LEFT, base_margin)
        self.sizer_pathlist.AddSpacer(12)

        # カスタム区切り線（薄いグレー）  ※ wx.Panelを「線のような矩形」として利用
        line_custom = wx.Panel(self, size=(-1, 1))
        line_custom.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.sizer_pathlist.Add(line_custom, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, base_margin)
        self.sizer_pathlist.AddSpacer(12)

        # OK/Cancelボタン
        self.btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_ok = wx.Button(self, wx.ID_OK, label=BTN_OK)
        self.btn_ok.Enable(bool(valid_args))
        self.btn_cancel = wx.Button(self, wx.ID_CANCEL, label=BTN_CANCEL)
        self.btn_sizer.Add(self.btn_ok, 0, wx.ALL, 5)
        self.btn_sizer.Add(self.btn_cancel, 0, wx.ALL, 5)

        # 初期表示設定（メインSizerにUI追加）
        self.main_sizer.Add(self.sizer_pathlist, 0, wx.EXPAND)
        self.main_sizer.Add(self.btn_sizer, 0, wx.ALIGN_CENTER)
        self.SetSizer(self.main_sizer)
        self.SetFont(self.font)
        self.Layout()
        self.Fit()
        self.Center()    # 画面中央に配置
        self.Raise()     # 最前面に表示
        self.SetDropTarget(MyFileDropTarget(self))    # ドロップターゲットを設定
        self.btn_ok.SetFocus()

# --------------------------------------
# ＯＫボタン押下後の処理（メインダイアログ）
# --------------------------------------
def handle_main_dialog_result(dlg_mode):
    target_type = 'file' if dlg_mode.rb_file.GetValue() else 'folder'    # 対象がFileかFolderか判定
    include_subfolders = dlg_mode.rb_include.GetValue()                  # サブフォルダを含めるか否か判定

    # テキスト/CSV出力
    output_data = collect_paths(valid_args, target_type, include_subfolders)
    out_path = export_list_to_text(output_data, target_type, dlg_mode, language_code)    # 出力処理

    # 完了ダイアログの表示処理（出力後の通知）
    show_completion_dialog(out_path)

    dlg_mode.Destroy()

# --------------------------------------
# 出力処理
# --------------------------------------
def export_list_to_text(output_data, target_type, dlg_mode, language_code):

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    out_filename = f"{'FilesPathList' if target_type == 'file' else 'FoldersPathList'}_{timestamp}.txt"
    out_path = os.path.join(desktop, out_filename)

    # 絵文字・特殊記号などシフトJISで表現できない文字が含まれている場合にエラーになるので日本語ではもshift_jisにしない
    encoding = 'utf-8-sig'
    with open(out_path, 'w', encoding=encoding, newline='') as f:
        for row in output_data:
            f.write(row + "\n")

    return out_path

# --------------------------------------
# 完了ダイアログ（出力結果の表示用クラス）
# --------------------------------------
class CompleteDialog(wx.Dialog):
    def __init__(self, parent, filepath):
        super().__init__(parent, title=APP_TITLE, style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.filepath = filepath
        sizer = wx.BoxSizer(wx.VERTICAL)
        msg = wx.StaticText(self, label=f"{MSG_COMPLETE}\n{filepath}")
        sizer.Add(msg, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_open = wx.Button(self, label=BTN_OPEN)
        self.btn_open.Bind(wx.EVT_BUTTON, self.on_open)
        btn_sizer.Add(self.btn_open, 0, wx.RIGHT, 10)
        self.btn_close = wx.Button(self, label=BTN_CLOSE)
        self.btn_close.Bind(wx.EVT_BUTTON, lambda evt: self.EndModal(wx.ID_CANCEL))
        btn_sizer.Add(self.btn_close, 0)
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        self.Center()    # 画面中央に配置
        self.Raise()     # 最前面に表示

    def on_open(self, event):
        try:
            os.startfile(self.filepath)
        except Exception as e:
            wx.MessageBox(f"{MSG_OPEN_ERROR}\n{e}", MSG_ERROR, wx.OK | wx.ICON_ERROR)
        finally:
            self.EndModal(wx.ID_OK)

# --------------------------------------
# 完了ダイアログの表示処理（出力後の通知）
# --------------------------------------
def show_completion_dialog(out_path):
    dlg_complete = CompleteDialog(None, out_path)
    dlg_complete.Center()    # 画面中央に配置
    dlg_complete.Raise()     # 最前面に表示
    dlg_complete.ShowModal()
    dlg_complete.Destroy()

# --------------------------------------
# メイン処理
# --------------------------------------
def main():
    global valid_args, LABEL_ARGS

    #コマンドライン引数を取得しargsに格納（最初の要素は実行ファイルパスなので除外）
    args = sys.argv[1:]

    # コマンドライン引数検証
    valid_args = validate_args(args)

    # 有効なコマンドライン引数があればLABEL_ARGSを更新
    if valid_args:
        LABEL_ARGS = L["LABEL_ARGS_TRUE"]

    # wxPythonアプリケーションオブジェクトを生成（必ず最初に作成する必要あり）
    app = wx.App(False)

    # メインダイアログ表示
    dlg_mode = MainDialog(None)
    # preload_all_async()         # 遅延ロード対象がなくなった（threadingのインポートも不要）
    res = dlg_mode.ShowModal()    # ユーザーがOKまたはキャンセルを選択するまで待機
    if res != wx.ID_OK:
        dlg_mode.Destroy()
        return

    # ＯＫボタン押下後の処理（メインダイアログ）
    handle_main_dialog_result(dlg_mode)

if __name__ == "__main__":
    main()
