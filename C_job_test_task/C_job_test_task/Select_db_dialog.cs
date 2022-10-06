using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_job_test_task
{
    public partial class Select_db_dialog : Form
    {
        string selectedDB;

        public string SelectedDB { get => selectedDB; }

        public Select_db_dialog()
        {
            InitializeComponent();
            this.selectedDB = "";

        }
        public void SetDbListValues(string[] files_list)
        {
            this.select_db_listBox.Items.AddRange(files_list);
        }
        private void select_db_file_btn_Click(object sender, EventArgs e)
        {
            if (this.select_db_listBox.SelectedItem!=null)
            {
                this.selectedDB = this.select_db_listBox.SelectedItem.ToString();
                this.Close();
            }
            else
            {
                MessageBox.Show("Please select one of the databases or create new one", "DB Select error", MessageBoxButtons.OK);
            }
            
           
        }

        private string validate_db_name(string raw_value)
        {
            for (int i = 0; i < raw_value.Length; i++)
            {
                if (!Char.IsLetterOrDigit(raw_value[i]))
                {
                    raw_value = raw_value.Replace(raw_value[i], ' ');
                }
              
            }
            raw_value = raw_value.Trim();
            return raw_value;
        }
        private void Create_new_DB_btn_Click(object sender, EventArgs e)
        {
            string new_db_name = this.new_db_name_txt_box.Text;
            new_db_name = validate_db_name(new_db_name)+".db";
            Database_creator db_creator = new Database_creator(new_db_name);
            new_db_name = Directory.GetCurrentDirectory() + "\\" + new_db_name;
            SetDbListValues(new string[] { new_db_name });
            this.selectedDB = new_db_name;
            

        }
    }
}
