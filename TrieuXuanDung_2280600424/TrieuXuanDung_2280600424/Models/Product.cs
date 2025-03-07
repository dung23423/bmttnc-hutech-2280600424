using System.ComponentModel.DataAnnotations;

namespace TrieuXuanDung_2280600424.Models
{
    public class Product
    {
        public int Id { get; set; }

        [Required]
        [StringLength(100)]
        public string Name { get; set; } = string.Empty;

        [StringLength(500)]
        public string? Description { get; set; }

        [Range(0.01, 10000.00)]
        public decimal Price { get; set; }

        public string? ImageUrl { get; set; }

        public bool IsNew { get; set; }

        public bool IsAvailable { get; set; } = true;

        public int? CategoryId { get; set; }
        public Category? Category { get; set; }
    }
}