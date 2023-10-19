import tkinter as tk
from itertools import zip_longest
'''
padx/pady 水平/垂直距离窗口间隔
draw_window 通过主frame, 构建2个水平排布的副frame

'''

class Parse_Window(object):
    def __init__(self, *args):
        root = tk.Tk()
        root.title("Window")
    
        main_frame = tk.Frame(root)
        main_frame.pack(side=tk.TOP, padx=10, pady=10)
        
        frame_left = tk.Frame(main_frame)
        frame_left.pack(side=tk.LEFT, padx=10, pady=10)

        self.entry_left = tk.Entry(frame_left, width=80)
        self.entry_left.pack(pady=10)

        self.text_left = Parse_Window.create_scrollbar_text(frame_left)
        
        frame_right = tk.Frame(main_frame)
        frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        self.entry_right = tk.Entry(frame_right, width=80)
        self.entry_right.pack(pady=10)

        self.text_right = Parse_Window.create_scrollbar_text(frame_right)

        #按钮
        parse_btn = tk.Button(text="解析", width=50, command=self.parse_input, bg="green", fg="white", font=("Helvetica", 16), bd=5)
        parse_btn.pack(pady=10)
        
        self.create_font_style()
        
        root.mainloop()
    
    black_font = "black"
    orange_font = "orange"
    red_font = "red"
    def create_font_style(self):
        font_style = ("Helvetica", 14)
        self.text_left.tag_config("black", foreground=Parse_Window.black_font,font=font_style)
        self.text_left.tag_config("orange", foreground=Parse_Window.orange_font,font=font_style)
        self.text_left.tag_config("red", foreground=Parse_Window.red_font,font=font_style)
        
        self.text_right.tag_config("black", foreground=Parse_Window.black_font,font=font_style)
        self.text_right.tag_config("orange", foreground=Parse_Window.orange_font,font=font_style)
        self.text_right.tag_config("red", foreground=Parse_Window.red_font,font=font_style)
    
    @staticmethod
    def create_scrollbar_text(root):
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # 创建Text控件，并关联滚动条
        text = tk.Text(root, wrap=tk.NONE, yscrollcommand=scrollbar.set, height=50)
        text.pack(pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 将滚动条的移动与Text控件的视图移动关联起来
        scrollbar.config(command=text.yview)
        return text
    
    def parse_input(self):
        entry_left_text = self.entry_left.get()
        left_text_list = Parse_Window.parse_entry_text(entry_left_text)

        entry_right_text = self.entry_right.get()
        right_text_list = Parse_Window.parse_entry_text(entry_right_text)
        
        self.text_left.delete("1.0", tk.END)
        self.text_right.delete("1.0", tk.END)
        
        for l,r in zip_longest(left_text_list, right_text_list):
            if l == r:
                if l != None:
                    self.text_left.insert(tk.END, l, Parse_Window.black_font)
                if r != None:
                    self.text_right.insert(tk.END, r, Parse_Window.black_font)
            else:
                if l != None:
                    self.text_left.insert(tk.END, l, Parse_Window.orange_font)
                if r != None:
                    self.text_right.insert(tk.END, r, Parse_Window.red_font)
        
    
    # 清空Text组件，并添加        
    @staticmethod
    def clear_and_intsert_text(text_tk, text):
        text_tk.delete("1.0", tk.END)
        text_tk.insert(tk.END, text)
                
    parse_data_length = 167
    @staticmethod
    def parse_entry_text(text:str):
        res = []
        if text == '':
            res.append("请输入解析文本")
            return res
        text_arr = text.split(',')
        if len(text_arr) != Parse_Window.parse_data_length:
            res.append(f'解析文本长度不正确,需要长度:{Parse_Window.parse_data_length}')
            return res
           
        start_idx = -1 
             
        # res.append(f'CameraHash:{text_arr[++start_idx]}\n')
        # res.append(f'PlayerAllBuffHash:{text_arr[++start_idx]}\n')
        # res.append(f'PlayerStatsHash:{text_arr[++start_idx]}\n')
        # res.append(f'AllEnemyHash:{text_arr[++start_idx]}\n')
        # res.append(f'TsMiscHash:{text_arr[++start_idx]}\n')
        # res.append(f'TsBulletHash:{text_arr[++start_idx]}\n')
        # res.append(f'ActivityScore:{text_arr[++start_idx]}\n')
        
        # transform
        res.append(f'PerSecUpdateTick:{text_arr[++start_idx]}\n')
        res.append(f'PerSecUpdateEventTimer:{text_arr[++start_idx]}\n')
        transform_content_list = []
        transform_content_count = 6
        for idx in range(1, transform_content_count + 1):
            transform_last_idx = idx + start_idx
            transform_content_list.append(text_arr[transform_last_idx])
        transform_content = str.join(',', transform_content_list)
        transform_str = f'[{transform_content}]'
        res.append(f'transform:{transform_str}\n')
        
        # 剩余的
        transform_last_idx += 1
        remind_arr = text_arr[transform_last_idx:]
        for remind in remind_arr:
            res.append(f'{remind}\n')
        return res
    
if __name__ == '__main__':
    parse_window = Parse_Window()
    