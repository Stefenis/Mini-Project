
# Memory blocks 
memory_blocks = {}

# Allocated blocks 
allocated_blocks = {}

# initialize memory blocks
def initialize_memory_blocks():
    """Initialize memory blocks with user input."""
    global memory_blocks
    print("\nInitialize Memory Blocks")
    try:
        num_blocks = int(input("Enter the number of memory blocks: "))
        for _ in range(num_blocks):
            size = int(input("Enter block size (in KB): "))
            if size not in memory_blocks:
                memory_blocks[size] = []
            memory_blocks[size].append(f"Block {size}_{len(memory_blocks[size]) + 1}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Allocation function
def allocate_memory(size):
    """Allocates memory for the given size."""
    # Check if there's an exact match list
    if size in memory_blocks and memory_blocks[size]:
        block = memory_blocks[size].pop(0)
        allocated_blocks[size] = block
        print(f"Allocated {size} KB to {block}.")
    else:
        # Best fit fallback if no exact match is found
        best_fit_size = None
        for block_size in memory_blocks:
            if block_size >= size and memory_blocks[block_size]:
                if best_fit_size is None or block_size < best_fit_size:
                    best_fit_size = block_size

        if best_fit_size is not None:
            block = memory_blocks[best_fit_size].pop(0)
            allocated_blocks[size] = block
            print(f"Allocated {size} KB to {block} using best-fit.")

            # Split the block if needed
            remaining_size = best_fit_size - size
            if remaining_size > 0:
                if remaining_size not in memory_blocks:
                    memory_blocks[remaining_size] = []
                memory_blocks[remaining_size].append(f"Remaining from {block}")
        else:
            print(f"Unable to allocate memory for {size} KB.")

# Display current memory state
def display_memory_state():
    print("\nAllocated Blocks:")
    for size, block in allocated_blocks.items():
        print(f"{size} KB: {block}")

    print("\nFree Blocks:")
    for size, blocks in memory_blocks.items():
        if blocks:
            print(f"{size} KB List: {blocks}")

# Main function 
def main():
    initialize_memory_blocks()
    while True:
        print("\nQuick Fit Memory Allocation System")
        print("1. Allocate Memory")
        print("2. View Memory State")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                size = int(input("Enter memory size to allocate (in KB): "))
                allocate_memory(size)
            except ValueError:
                print("Invalid size. Please enter a valid number.")
        elif choice == '2':
            display_memory_state()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
