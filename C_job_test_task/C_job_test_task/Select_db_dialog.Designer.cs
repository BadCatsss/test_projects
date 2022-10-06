namespace C_job_test_task
{
    partial class Select_db_dialog
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.select_db_listBox = new System.Windows.Forms.ListBox();
            this.select_db_file_btn = new System.Windows.Forms.Button();
            this.Create_new_DB_btn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.new_db_name_txt_box = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // select_db_listBox
            // 
            this.select_db_listBox.FormattingEnabled = true;
            this.select_db_listBox.ItemHeight = 16;
            this.select_db_listBox.Location = new System.Drawing.Point(12, 24);
            this.select_db_listBox.Name = "select_db_listBox";
            this.select_db_listBox.Size = new System.Drawing.Size(592, 404);
            this.select_db_listBox.TabIndex = 0;
            // 
            // select_db_file_btn
            // 
            this.select_db_file_btn.Location = new System.Drawing.Point(610, 112);
            this.select_db_file_btn.Name = "select_db_file_btn";
            this.select_db_file_btn.Size = new System.Drawing.Size(178, 23);
            this.select_db_file_btn.TabIndex = 1;
            this.select_db_file_btn.Text = "Select and open DB";
            this.select_db_file_btn.UseVisualStyleBackColor = true;
            this.select_db_file_btn.Click += new System.EventHandler(this.select_db_file_btn_Click);
            // 
            // Create_new_DB_btn
            // 
            this.Create_new_DB_btn.Location = new System.Drawing.Point(610, 185);
            this.Create_new_DB_btn.Name = "Create_new_DB_btn";
            this.Create_new_DB_btn.Size = new System.Drawing.Size(178, 23);
            this.Create_new_DB_btn.TabIndex = 2;
            this.Create_new_DB_btn.Text = "Create new DB";
            this.Create_new_DB_btn.UseVisualStyleBackColor = true;
            this.Create_new_DB_btn.Click += new System.EventHandler(this.Create_new_DB_btn_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(622, 232);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(96, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "New DB name:";
            // 
            // new_db_name_txt_box
            // 
            this.new_db_name_txt_box.Location = new System.Drawing.Point(625, 271);
            this.new_db_name_txt_box.Name = "new_db_name_txt_box";
            this.new_db_name_txt_box.Size = new System.Drawing.Size(163, 22);
            this.new_db_name_txt_box.TabIndex = 4;
            // 
            // Select_db_dialog
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.new_db_name_txt_box);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Create_new_DB_btn);
            this.Controls.Add(this.select_db_file_btn);
            this.Controls.Add(this.select_db_listBox);
            this.Name = "Select_db_dialog";
            this.Text = "Select_db_dialog";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox select_db_listBox;
        private System.Windows.Forms.Button select_db_file_btn;
        private System.Windows.Forms.Button Create_new_DB_btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox new_db_name_txt_box;
    }
}