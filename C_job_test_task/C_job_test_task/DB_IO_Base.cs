using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_job_test_task
{
    internal class DB_IO_Base
    {
        protected SQLiteConnection db_connection;
        public DB_IO_Base(string db_file_path)
        {
            if (File.Exists(db_file_path))
            {

                db_connection = new SQLiteConnection("Data Source=" + db_file_path);
                db_connection.Open();
            }
        }
        protected void CheckConnection()
        {
            if (db_connection.State == System.Data.ConnectionState.Closed)
            {
                db_connection.Open();
            }
            else if (db_connection.State == System.Data.ConnectionState.Broken)
            {
                db_connection.Close();
                db_connection.Open();
            }
        }
        public string[] Get_DB_SChema(string table)
        {
            CheckConnection();
            string get_schema_command = "SELECT * FROM " + table;
            List<string> columns_names = new List<string>();
            SQLiteCommand Command = new SQLiteCommand(get_schema_command, db_connection);
            var dr = Command.ExecuteReader();
            for (var i = 0; i < dr.FieldCount; i++)
            {
                columns_names.Add(dr.GetName(i));
            }
            return columns_names.ToArray();
        }
    }

}
