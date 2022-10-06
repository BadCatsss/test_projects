using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_job_test_task
{
    public partial class Form1 : Form
    {
        private Database_Loader db_loader;
        string[] default_column_names;
        public Form1()
        {
            InitializeComponent();
            db_loader = new Database_Loader();
            default_column_names = Database_creator.Db_defualt_scheme.Keys.ToArray();

        }

        private void Add_to_database_btn_Click(object sender, EventArgs e)
        {
            var childs = this.add_to_db_groupBox.Controls;
            string ship_id = ship_set_id_textbox.Text;
            string ship_name = ship_set_name_textbox.Text;
            string ship_length = ship_set_length_textbox.Text;
            string ship_breadth = ship_set_breadth_textbox.Text;
            string ship_depth = ship_set_depth_textbox.Text;
            DataValidator dataValidator = new DataValidator();
            bool ship_id_is_valid=dataValidator.validate_value(ship_id, new Dictionary<DataValidator.DataConstraints, int> { { DataValidator.DataConstraints.only_digits, 0 } });
            bool ship_name_is_valid=dataValidator.validate_value(ship_name, new Dictionary<DataValidator.DataConstraints, int> { { DataValidator.DataConstraints.only_letters, 0 } });
            bool ship_length_is_valid=dataValidator.validate_value(ship_length, new Dictionary<DataValidator.DataConstraints, int> { { DataValidator.DataConstraints.bigger_than, 0 }, { DataValidator.DataConstraints.smaller_than, 362 } });
            bool ship_breath_is_valid=dataValidator.validate_value(ship_breadth, new Dictionary<DataValidator.DataConstraints, int> { { DataValidator.DataConstraints.bigger_than, 0 }, { DataValidator.DataConstraints.smaller_than, 33 }  });
            bool ship_depth_is_valid=dataValidator.validate_value(ship_depth, new Dictionary<DataValidator.DataConstraints, int> { { DataValidator.DataConstraints.bigger_than, 0 }, { DataValidator.DataConstraints.smaller_than, 24}  });

            Database_writer db_writer = new Database_writer(db_loader.Loaded_databse_path);
            var loaded_db_column_names=db_writer.Get_DB_SChema(Database_creator.db_default_table_name);
           
            bool db_schema_is_valid = loaded_db_column_names.SequenceEqual(default_column_names);
            bool write_result = false;

            if (db_schema_is_valid && ship_id_is_valid && ship_name_is_valid && ship_length_is_valid && ship_breath_is_valid && ship_depth_is_valid)
            {
                Dictionary<string,string> insert_value_dictionary = new Dictionary<string,string>();
                List<string> values_for_insert = new List<string>();
                values_for_insert.Add(ship_id);
                values_for_insert.Add(ship_name);
                values_for_insert.Add(ship_length);
                values_for_insert.Add(ship_breadth);
                values_for_insert.Add(ship_depth);
                for (int i = 0; i < default_column_names.Length; i++)
                {
                    insert_value_dictionary[default_column_names[i]] = values_for_insert[i];
                }

                write_result=db_writer.Write_to_db(Database_creator.db_default_table_name, insert_value_dictionary);
            }
            if (write_result)
            {
                MessageBox.Show("New Record successfully was add.", "New record was add", MessageBoxButtons.OK);
            }
            else
            {
                MessageBox.Show("Error in inserted data. Please check your input:\n id - must be integer\n" +
                    "ship name - must contains only charters\n ship length - must be > 0 and < 362\n " +
                    "ship breadth - must be > 0 and < 33\n sheep depth - must be > 0 and < 24", "New record was NOT add", MessageBoxButtons.OK);
            }
        }

        private void Ship_get_ID_button_Click(object sender, EventArgs e)
        {
            string ship_id_val = this.Ship_ID__get_textBox.Text;
            Database_Reader db_reader = new Database_Reader(db_loader.Loaded_databse_path);
            var db_data=db_reader.Read_From_Database(Database_creator.db_default_table_name, new List<string> { "*" }, new Dictionary<string, string> { { "id",ship_id_val } });
            string db_data_data_str = "";
            for (int i = 0; i < db_data.Length; i++)
            {
                db_data_data_str += db_data[i];
            }
            if (db_data_data_str=="")
            {
                MessageBox.Show("Record not found for this ID", "Record not found", MessageBoxButtons.OK);
            }
            this.Ship_ID_get_info_textBox.Text = db_data_data_str;
        }
    }
}
