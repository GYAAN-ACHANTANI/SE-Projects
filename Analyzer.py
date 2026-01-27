import customtkinter as ctk
from tkinter import messagebox
import webbrowser

# --- Theme Configuration ---
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class SkillNovaPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SkillNova Pro | Enterprise Placement Suite")
        self.geometry("1280x950")
        
        # Style Constants
        self.navy_blue = "#1e3a8a"
        self.accent_green = "#10b981"
        self.border_gray = "#e2e8f0"
        self.text_dark = "#0f172a"
        
        # State Management
        self.history = []
        self.user_name = ctk.StringVar()
        self.user_skills = ctk.StringVar()
        self.selected_company = ctk.StringVar()
        self.star_rating = 0
        self.readiness_score = 0.0
        
        # Company Skills Database
        self.company_requirements = {
            "Google": ["System Design", "Advanced DSA", "Go/C++", "Cloud Architecture"],
            "Deloitte": ["SQL", "Business Intelligence", "Power BI", "Agile Methodology"],
            "Microsoft": ["C#/.NET", "Azure Fundamentals", "Enterprise Security", "Typescript"],
            "TCS": ["Java Fullstack", "DBMS", "Core Python", "Software Testing"],
            "Default": ["Generative AI", "Full Stack Development", "Operating Systems", "Networking"]
        }

        self.main_container = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_container.pack(fill="both", expand=True)
        self.render_landing()

    def navigate_to(self, page_func, *args, **kwargs):
        if not self.history or self.history[-1][0] != page_func:
            self.history.append((page_func, args, kwargs))
        page_func(*args, **kwargs)

    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()
            prev_page, args, kwargs = self.history.pop()
            self.navigate_to(prev_page, *args, **kwargs)

    def clear(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
        if len(self.history) > 1:
            back_btn = ctk.CTkButton(self.main_container, text="← Back", width=80, height=30, 
                                    fg_color="transparent", text_color=self.navy_blue, 
                                    border_width=1, border_color=self.navy_blue, command=self.go_back)
            back_btn.place(x=30, y=30)

    # --- 1. LANDING PAGE ---
    def render_landing(self):
        self.clear()
        self.history = [(self.render_landing, (), {})]
        ctk.CTkLabel(self.main_container, text="SKILLNOVA", font=("Inter", 82, "bold"), text_color=self.navy_blue).pack(pady=(120, 0))
        ctk.CTkLabel(self.main_container, text="YOUR CAREER, ENGINEERED. BRIDGING THE GAP TO THE ELITE.", 
                     font=("Inter", 18, "italic"), text_color="#64748b").pack(pady=(5, 30))

        f_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        f_frame.pack(pady=20)
        features = [("🎯 Precise Analytics", "Gap detection"), ("⚡ Rapid Booking", "Slot management"), ("📚 Curated Mastery", "YouTube roadmaps")]
        for title, sub in features:
            box = ctk.CTkFrame(f_frame, fg_color="#f8fafc", corner_radius=12, width=200, height=100)
            box.pack(side="left", padx=15)
            box.pack_propagate(False)
            ctk.CTkLabel(box, text=title, font=("Inter", 14, "bold"), text_color=self.navy_blue).pack(pady=(20,0))
            ctk.CTkLabel(box, text=sub, font=("Inter", 12), text_color="gray").pack()

        ctk.CTkButton(self.main_container, text="Begin Your Journey", height=60, width=320, 
                      fg_color=self.navy_blue, font=("Inter", 20, "bold"), 
                      command=lambda: self.navigate_to(self.render_login)).pack(pady=60)

    # --- 2. LOGIN ---
    def render_login(self):
        self.clear()
        card = ctk.CTkFrame(self.main_container, width=400, height=400, fg_color="white", border_width=1, border_color=self.border_gray)
        card.place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkLabel(card, text="Student Identity", font=("Inter", 26, "bold"), text_color=self.navy_blue).pack(pady=30)
        self.name_in = ctk.CTkEntry(card, placeholder_text="Full Name", width=300, height=45)
        self.name_in.pack(pady=10)
        ctk.CTkButton(card, text="Access Portal", width=300, height=45, fg_color=self.navy_blue, 
                      command=lambda: self.auth()).pack(pady=30)

    def auth(self):
        if self.name_in.get():
            self.user_name.set(self.name_in.get())
            self.navigate_to(self.render_details)

    # --- 3. ACADEMIC PROFILE ---
    def render_details(self):
        self.clear()
        ctk.CTkLabel(self.main_container, text="Academic Roadmap", font=("Inter", 32, "bold"), text_color=self.navy_blue).pack(pady=40)
        form = ctk.CTkFrame(self.main_container, width=550, fg_color="#f8fafc", border_width=1)
        form.pack(pady=10)
        self.branch_sel = ctk.CTkOptionMenu(form, values=["Computer Science", "IT", "AI & DS"], width=350, fg_color=self.navy_blue)
        self.branch_sel.pack(pady=15)
        self.year_sel = ctk.CTkOptionMenu(form, values=["Third Year", "Final Year"], width=350, fg_color=self.navy_blue)
        self.year_sel.pack(pady=15)
        self.sk_in = ctk.CTkEntry(form, placeholder_text="Enter Your Current Skills (Comma Separated)", width=350, height=45)
        self.sk_in.pack(pady=20)
        ctk.CTkButton(self.main_container, text="Find Opportunities", height=50, width=250, fg_color=self.navy_blue, 
                      command=lambda: self.navigate_to(self.render_company_selection)).pack(pady=30)

    # --- 4. COMPANY SELECTION ---
    def render_company_selection(self):
        self.user_skills.set(self.sk_in.get())
        self.clear()
        ctk.CTkLabel(self.main_container, text="Select Target Path", font=("Inter", 32, "bold"), text_color=self.navy_blue).pack(pady=40)
        
        grid = ctk.CTkFrame(self.main_container, fg_color="transparent")
        grid.pack()
        for i, c in enumerate(["Google", "Deloitte", "Microsoft", "TCS"]):
            btn = ctk.CTkButton(grid, text=c, width=220, height=120, corner_radius=12, fg_color="#f1f5f9", 
                               text_color=self.navy_blue, border_width=1, border_color=self.navy_blue,
                               command=lambda x=c: self.route_selection(x, False))
            btn.grid(row=i//2, column=i%2, padx=15, pady=15)
        
        ctk.CTkLabel(self.main_container, text="OR enter your Dream Company:").pack(pady=(30, 5))
        self.dream_in = ctk.CTkEntry(self.main_container, placeholder_text="Company Name", width=470, height=45)
        self.dream_in.pack(pady=10)
        ctk.CTkButton(self.main_container, text="Generate Skill Gap Report", width=470, height=45, fg_color=self.text_dark, 
                      command=lambda: self.route_selection(self.dream_in.get(), True)).pack()

    def route_selection(self, name, custom):
        if not name: return
        self.selected_company.set(name)
        if custom:
            self.calculate_readiness(name)
            self.navigate_to(self.render_gap_report)
        else:
            self.navigate_to(self.render_slot_booking)

    def calculate_readiness(self, name):
        user_list = [s.strip().lower() for s in self.user_skills.get().split(",")]
        required_list = self.company_requirements.get(name, self.company_requirements["Default"])
        matches = sum(1 for skill in required_list if skill.lower() in user_list)
        self.readiness_score = matches / len(required_list) if len(required_list) > 0 else 0.0

    # --- 5. INTERVIEW SLOT BOOKING ---
    def render_slot_booking(self):
        self.clear()
        ctk.CTkLabel(self.main_container, text=f"Interview Scheduler: {self.selected_company.get()}", 
                     font=("Inter", 32, "bold"), text_color=self.navy_blue).pack(pady=40)
        
        slot_card = ctk.CTkFrame(self.main_container, width=500, height=300, fg_color="#f8fafc", border_width=1)
        slot_card.pack(pady=20)
        
        self.slot_var = ctk.StringVar(value="Choose a time slot")
        slots = ["Feb 12, 10:00 AM", "Feb 12, 02:00 PM", "Feb 13, 09:00 AM", "Feb 14, 11:30 AM"]
        ctk.CTkOptionMenu(slot_card, values=slots, variable=self.slot_var, width=300, fg_color=self.navy_blue).pack(pady=40)
        
        ctk.CTkButton(slot_card, text="Confirm Booking", height=45, width=200, fg_color=self.accent_green,
                      command=self.confirm_booking).pack(pady=10)

    def confirm_booking(self):
        if self.slot_var.get() == "Choose a time slot": return
        messagebox.showinfo("Success", f"Your slot of {self.slot_var.get()} is booked. All the best!")
        self.navigate_to(self.render_feedback)

    # --- 6. DETAILED GAP REPORT ---
    def render_gap_report(self):
        self.clear()
        needed = self.company_requirements.get(self.selected_company.get(), self.company_requirements["Default"])
        ctk.CTkLabel(self.main_container, text=f"Gap Analysis: {self.selected_company.get()}", font=("Inter", 32, "bold"), text_color=self.navy_blue).pack(pady=20)
        
        # Skill Graph
        graph = ctk.CTkFrame(self.main_container, fg_color="#f1f5f9", width=700, height=120)
        graph.pack(pady=10)
        ctk.CTkLabel(graph, text=f"Readiness Score: {int(self.readiness_score*100)}%", font=("Inter", 16, "bold"), text_color=self.navy_blue).pack(pady=5)
        progress = ctk.CTkProgressBar(graph, width=600, height=20, progress_color=self.accent_green)
        progress.set(self.readiness_score)
        progress.pack(pady=10)
        
        # Mastery Roadmap
        ctk.CTkLabel(self.main_container, text="Recommended Mastery Courses", font=("Inter", 20, "bold")).pack(pady=20)
        c_frame = ctk.CTkFrame(self.main_container, fg_color="white", border_width=1)
        c_frame.pack(padx=100, fill="x")
        
        for skill in needed:
            row = ctk.CTkFrame(c_frame, fg_color="transparent")
            row.pack(fill="x", pady=5, padx=20)
            ctk.CTkLabel(row, text=f"• {skill} Expert Specialization", font=("Inter", 14)).pack(side="left")
            yt_link = f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+roadmap"
            ctk.CTkButton(row, text="Watch on YouTube", width=140, height=30, fg_color="#ef4444", 
                               command=lambda l=yt_link: webbrowser.open(l)).pack(side="right")

        # FIX: Added Proceed Button to move to Feedback
        ctk.CTkButton(self.main_container, text="Proceed to Final Portal", height=55, width=300, 
                      fg_color=self.navy_blue, font=("Inter", 16, "bold"),
                      command=lambda: self.navigate_to(self.render_feedback)).pack(pady=40)

    # --- 7. FEEDBACK PAGE ---
    def render_feedback(self):
        self.clear()
        ctk.CTkLabel(self.main_container, text="Experience Feedback", font=("Inter", 32, "bold"), text_color=self.navy_blue).pack(pady=40)
        
        star_f = ctk.CTkFrame(self.main_container, fg_color="transparent")
        star_f.pack(pady=10)
        self.star_btns = []
        for i in range(1, 6):
            btn = ctk.CTkButton(star_f, text="☆", width=40, font=("Inter", 35), fg_color="transparent", text_color=self.navy_blue, 
                               command=lambda x=i: self.update_stars(x))
            btn.pack(side="left", padx=10)
            self.star_btns.append(btn)

        self.fb_box = ctk.CTkTextbox(self.main_container, width=600, height=150, border_width=1)
        self.fb_box.pack(pady=30)
        ctk.CTkButton(self.main_container, text="Submit Report", height=60, width=300, fg_color=self.navy_blue, 
                      command=lambda: self.navigate_to(self.render_landing)).pack()

    def update_stars(self, count):
        self.star_rating = count
        for i, btn in enumerate(self.star_btns):
            btn.configure(text="★" if i < count else "☆")

if __name__ == "__main__":
    app = SkillNovaPro()
    app.mainloop()