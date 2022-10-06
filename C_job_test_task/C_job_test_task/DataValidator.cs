using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_job_test_task
{
    internal class DataValidator
    {
        public enum DataConstraints
        {
            only_letters,
            only_digits,
            bigger_than,
            smaller_than
        }
        public bool validate_value(string raw_value, Dictionary<DataConstraints,int> constrainsts_rules)
        {
            bool data_is_valid_flag = true;
            if (raw_value.Length==0)
            {
                return false;
            }
            foreach (var constraint in constrainsts_rules)
            {
                switch (constraint.Key)
                {
                    case DataConstraints.only_letters:
                        data_is_valid_flag=raw_value.All(Char.IsLetter);
                        break;
                    case DataConstraints.only_digits:
                        data_is_valid_flag = raw_value.All(Char.IsDigit);
                        break;
                    case DataConstraints.bigger_than:
                        if (!raw_value.All(Char.IsDigit) || Int32.Parse(raw_value)<constraint.Value)
                        {
                            data_is_valid_flag = false;
                        }
                        break;
                    case DataConstraints.smaller_than:
                        if (!raw_value.All(Char.IsDigit) || Int32.Parse(raw_value) > constraint.Value)
                        {
                            data_is_valid_flag = false;
                        }
                        break;
                    default:
                        break;
                }
            }
            return data_is_valid_flag;
        }
    }
}
