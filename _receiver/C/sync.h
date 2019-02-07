#include <stdint.h>
struct sync_buffer_struct { // Each channel has a circular buffer struct
	uint32_t delay;
	uint8_t *circ_buffer;  // Circular buffer	
};


