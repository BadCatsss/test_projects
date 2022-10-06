using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_job_test_task
{
    internal class Database_Loader
    {
        private string loaded_databse_path="";
        public Database_Loader()
        {
            var found_dtabases_files=Directory.GetFiles(Directory.GetCurrentDirectory(), "*.db");
            bool is_databasse_file_found=Convert.ToBoolean(found_dtabases_files.Length);
            if (is_databasse_file_found)
            {
                Select_db_dialog open_db_dialog = new Select_db_dialog();
                open_db_dialog.SetDbListValues(found_dtabases_files);
                string message = "*.db files was find in current directory. Plese select db from list or create new.";
                string msgNBoxCaption = "Database files was find";
                MessageBoxButtons buttons = MessageBoxButtons.OK;
                MessageBox.Show(message, msgNBoxCaption, buttons);
                open_db_dialog.ShowDialog();
                this.loaded_databse_path = open_db_dialog.SelectedDB;
            }
            else
            {
                string database_default_name = "test" + ".db";
                string message = "Database was not found. Was create and open new database:"+ database_default_name;
                string msgNBoxCaption = "Database was not found";
                MessageBoxButtons buttons = MessageBoxButtons.OK;
                MessageBox.Show(message, msgNBoxCaption, buttons);
                string db_full_path = Directory.GetCurrentDirectory() + "\\" + database_default_name;
                Database_creator db_creator = new Database_creator(db_full_path);
                this.loaded_databse_path = db_full_path;
            }
            MessageBox.Show("Was select database:\n " + this.loaded_databse_path, "Database was select", MessageBoxButtons.OK);
        }

        public string Loaded_databse_path { get => loaded_databse_path; set => loaded_databse_path = value; }
    }
}
