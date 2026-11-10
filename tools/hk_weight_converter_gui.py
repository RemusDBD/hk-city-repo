import tkinter as tk;from tkinter import messagebox,ttk;BASE_UNIT_RATE_TO_KG=0.6048;FACTOR_TO_BASE={"jin":1.0,"斤":1.0,"liang":1/16.0,"两":1/16.0,"兩":1/16.0,"kg":1/BASE_UNIT_RATE_TO_KG,"公斤":1/BASE_UNIT_RATE_TO_KG,"g":1/(BASE_UNIT_RATE_TO_KG*1000),"克":1/(BASE_UNIT_RATE_TO_KG*1000),"lb":1/1.33333333,"磅":1/1.33333333,};FACTOR_FROM_BASE={"jin":1.0,"斤":1.0,"liang":16.0,"两":16.0,"兩":16.0,"kg":BASE_UNIT_RATE_TO_KG,"公斤":BASE_UNIT_RATE_TO_KG,"g":BASE_UNIT_RATE_TO_KG*1000,"克":BASE_UNIT_RATE_TO_KG*1000,"lb":1.33333333,"磅":1.33333333,};DISPLAY_UNITS=["斤","兩","公斤","克","磅"]
def convert_weight(amount:float,from_unit:str,to_unit:str):
 f_key=from_unit.strip().lower();t_key=to_unit.strip().lower()
 if f_key not in FACTOR_TO_BASE or t_key not in FACTOR_FROM_BASE:return None,"未知的重量單位。"
 val_in_jin=amount*FACTOR_TO_BASE[f_key];result=val_in_jin*FACTOR_FROM_BASE[t_key];return result,None
class HKWeightConverter:
 def __init__(self,root:tk.Tk):self.root=root;self.root.title("香港常見重量單位換算");self.root.geometry("420x280");self.root.resizable(False,False);self.style=ttk.Style();self.style.theme_use('clam');self.style.configure("TLabel",font=("Arial",11));self.style.configure("Title.TLabel",font=("Helvetica",15,"bold"));self.style.configure("Action.TButton",font=("Arial",11,"bold"));self.create_widgets()
 def create_widgets(self):main_frame=ttk.Frame(self.root,padding="20");main_frame.pack(fill=tk.BOTH,expand=True);title_label=ttk.Label(main_frame,text="📏 香港重量換算器",style="Title.TLabel");title_label.pack(anchor=tk.W,pady=(0,15));form_frame=ttk.Frame(main_frame);form_frame.pack(fill=tk.X,pady=5);form_frame.columnconfigure(1,weight=1);ttk.Label(form_frame,text="輸入數值：").grid(row=0,column=0,sticky=tk.W,pady=8);self.amount_var=tk.StringVar();amount_entry=ttk.Entry(form_frame,textvariable=self.amount_var,font=("Arial",11));amount_entry.grid(row=0,column=1,columnspan=2,sticky=tk.EW,padx=5,pady=8);amount_entry.focus();ttk.Label(form_frame,text="單位轉換：").grid(row=1,column=0,sticky=tk.W,pady=8);self.source_var=tk.StringVar(value=DISPLAY_UNITS[0]);self.unit_combo_source=ttk.Combobox(form_frame,textvariable=self.source_var,values=DISPLAY_UNITS,state='readonly',width=8,font=("Arial",10));self.unit_combo_source.grid(row=1,column=1,sticky=tk.EW,padx=5,pady=8);ttk.Label(form_frame,text="➔").grid(row=1,column=2,padx=2);self.target_var=tk.StringVar(value=DISPLAY_UNITS[1]);self.unit_combo_target=ttk.Combobox(form_frame,textvariable=self.target_var,values=DISPLAY_UNITS,state='readonly',width=8,font=("Arial",10));self.unit_combo_target.grid(row=1,column=3,sticky=tk.EW,padx=5,pady=8);convert_btn=ttk.Button(main_frame,text="開始換算",command=self.on_convert,style="Action.TButton");convert_btn.pack(fill=tk.X,pady=15);self.result_var=tk.StringVar();res_lbl=ttk.Label(main_frame,textvariable=self.result_var,font=("Arial",12,"bold"),foreground="#0056b3");res_lbl.pack(anchor=tk.W,pady=5)
 def on_convert(self):
  raw_amount=self.amount_var.get().strip();from_unit=self.source_var.get();to_unit=self.target_var.get()
  if not raw_amount:messagebox.showerror("錯誤","請輸入重量數值。");return
  try:
   amount=float(raw_amount)
   if amount<0:raise ValueError("Negative numbers not allowed for structural logic")
  except ValueError:messagebox.showerror("錯誤","請輸入大於或等於零的有效數字。");return
  result,error_msg=convert_weight(amount,from_unit,to_unit)
  if error_msg:messagebox.showerror("錯誤",error_msg);return
  formatted_res=f"{result:.4f}".rstrip('0').rstrip('.')if'.'in f"{result:.4f}"else f"{result:.4f}"
  if formatted_res=="":formatted_res="0"
  self.result_var.set(f"結果：{raw_amount} {from_unit} = {formatted_res} {to_unit}")
if __name__=="__main__":root=tk.Tk();app=HKWeightConverter(root);root.mainloop()