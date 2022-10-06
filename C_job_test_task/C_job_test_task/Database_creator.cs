using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Runtime.Remoting.Contexts;
using System.Text;
using System.Threading.Tasks;

namespace C_job_test_task
{

    internal class Database_creator
    {
        public enum Sqlite_Types
        {
            sqlite_int,
            sqlite_string,
            sqlite_float
        }
        private static Dictionary<string, Sqlite_Types> db_defualt_scheme = new Dictionary<string, Sqlite_Types> {
            { "id",Sqlite_Types.sqlite_int},
            { "name",Sqlite_Types.sqlite_string},
            { "length",Sqlite_Types.sqlite_int},
            { "breadth",Sqlite_Types.sqlite_int},
            { "depth",Sqlite_Types.sqlite_float}
        };
        private Dictionary<string, string> db_fields_constraints = new Dictionary<string, string> {
            { "id","PRIMARY KEY"},
            { "name","NOT NULL"},
            { "length","NOT NULL"},
            { "breadth","NOT NULL"},
            { "depth","NOT NULL"}
        };
        public static string db_default_table_name="ships";

        public static Dictionary<string, Sqlite_Types> Db_defualt_scheme { get => db_defualt_scheme; }

        private Dictionary<Sqlite_Types, string> sqlite_types_transform_dict = new Dictionary<Sqlite_Types, string> {
            { Sqlite_Types.sqlite_int,"INTEGER"},
            {Sqlite_Types.sqlite_float,"REAL"},
            {Sqlite_Types.sqlite_string,"TEXT"} };
        public Database_creator(string datbase_file_path)
        {
            if (Db_defualt_scheme.Count > 0)
            {
                if (!File.Exists(datbase_file_path))
                {
                    SQLiteConnection.CreateFile(datbase_file_path);
                }
}
                using (var connection = new SQLiteConnection("Data Source="+datbase_file_path))
                {
                    string create_table_command = "CREATE TABLE " + db_default_table_name + " (";
                    foreach (var scheme_el in db_defualt_scheme)
                    {
                        string filed_str=scheme_el.Key+" " + sqlite_types_transform_dict[scheme_el.Value]+" " + db_fields_constraints[scheme_el.Key]+" , ";
                        create_table_command += filed_str;
                    }
                create_table_command=create_table_command.Remove(create_table_command.Length - 2, 1);
                create_table_command += " );";
                    SQLiteCommand Command = new SQLiteCommand(create_table_command, connection);
                    connection.Open();
                    Command.ExecuteNonQuery();
                    connection.Close();
            }
            }
        }
 
}
