using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_job_test_task
{
    internal class Database_Reader : DB_IO_Base
    {
        public Database_Reader(string db_file_path) : base(db_file_path)
        {
            CheckConnection();

        }
        public string[] Read_From_Database(string table, List<string> table_columns, Dictionary<string, string> where_clause)
        {
            var default_schema = Database_creator.Db_defualt_scheme.Keys.ToArray();
            CheckConnection();
            string select_values_command = "";
            if (table_columns.Count == 1 && table_columns[0] == "*")
            {
                select_values_command = "SELECT * FROM " + table;

            }
            else
            {
                if (default_schema.Except(table_columns).Any())
                {

                    select_values_command = "SELECT " + table + " (";
                    foreach (var selected_key in table_columns)
                    {
                        select_values_command += selected_key + " ,";
                    }
                    select_values_command = select_values_command.Remove(select_values_command.Length - 1, 1);
                    select_values_command += " FROM " + table;
                }
                

            }
            string where_clause_part = "";
            if (where_clause.Count > 0)
            {
                if (default_schema.Except(where_clause.Keys).Any())
                {

                    where_clause_part = "WHERE ";
                    foreach (var where_q in where_clause)
                    {
                        where_clause_part += where_q.Key + " = " + where_q.Value + " AND ";

                    }
                    where_clause_part = where_clause_part.Remove(where_clause_part.Length - 5, 4);

                }

            }
            if (select_values_command != "")
            {
                select_values_command += " " + where_clause_part + " ;";

                SQLiteCommand insert_to_db = new SQLiteCommand(select_values_command, db_connection);
                SQLiteDataReader dataReader= insert_to_db.ExecuteReader();
                List<string> readed_data = new List<string>();
                while (dataReader.Read())
                {
                    for (int i = 0; i < default_schema.Length; i++)
                    {
                        readed_data.Add(default_schema[i]+" : "+Convert.ToString(dataReader[default_schema[i]])+"\r\n");
                    }
                    
                }
                

                return readed_data.ToArray();
            }
            return new string[0];
        }
    }
}
