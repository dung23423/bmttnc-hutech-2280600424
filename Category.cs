using System.ComponentModel.DataAnnotations;

namespace TrieuXuanDung_22800600424_B3.Models
{
    public class Category
    {
        public int Id { get; set; }
        [Required, StringLength(50)]
        public string Name { get; set; }
        public List<Product>? Products { get; set; }
    }
}
