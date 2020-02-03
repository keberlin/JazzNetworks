#include <stdlib.h>


struct node_t
{
    unsigned v;
    struct node_t* next;
};


struct node_t* even_nodes(struct node_t**list)
{
    node_t *new_list = NULL; // Return value
    node_t *prev_node = NULL, *last_node = NULL, *next_node;
    node_t *node = *list;

    // Reset the passed in (old) list
    *list = NULL;

    while (node)
    {
        // Keep track of the next node in the linked list
        next_node = node->next;

        // Remove this node from its current linked list
        node->next = NULL;

        // Check for even valued nodes (to move into new list)
        if (node->v%2 == 0)
        {
            // Move this node ino the new list
            if (new_list == NULL)
                // Keep track of the first node in the new list
                new_list = node;

            if (last_node)
                // Ensure the new linked list is maintained
                last_node->next = node;

            // Keep track of the last node in the new list
            last_node = node;
        }
        else
        {
            // Retain this node in the old list
            if (*list == NULL)
                // Keep track of the first node in the old list
                *list = node;

            if (prev_node)
                // Ensure the old linked list is maintained
                prev_node->next = node;

            // Keep track of the previous node in the old list
            prev_node = node;
        }

        // Advance onto the next node
        node = next_node;
    }

    // Return a pointer to the first node in new list
    return new_list;
}
