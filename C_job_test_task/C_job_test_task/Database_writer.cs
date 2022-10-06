using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_job_test_task
{
    internal class Database_writer : DB_IO_Base
    {
        public Database_writer(string db_file_path):base(db_file_path)
        {
            CheckConnection();
        }

        public bool Write_to_db(string table, Dictionary<string,string> values_for_write)
        {
            CheckConnection();
            string insert_values_command = "INSERT INTO "+table+" (";
            foreach (var inserted_key in values_for_write.Keys)
            {
                insert_values_command +=   inserted_key+" ,";
            }
            insert_values_command = insert_values_command.Remove(insert_values_command.Length - 1, 1);
            insert_values_command += " ) VALUES ( ";
            foreach (var inserted_value in values_for_write.Values)
            {
                insert_values_command +=  "'"+inserted_value+"'"+ " ,";
            }
            insert_values_command = insert_values_command.Remove(insert_values_command.Length - 1, 1);
            insert_values_command += " );";
            SQLiteCommand insert_to_db = new SQLiteCommand(insert_values_command, db_connection);
            insert_to_db.ExecuteNonQuery();
            return true;
        }
       
    }
}
