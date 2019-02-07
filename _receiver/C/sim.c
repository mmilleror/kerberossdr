/* KerberosSDR DAQ
 *
 * Copyright (C) 2018-2019  Carl Laufer, Tamás Pető
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

#define CH_NO 4 // Number of channels
#define BUFFER_SIZE 1024*512


int main()
{   
    fprintf(stderr, "Hydra test started \n");		
    int success = 1;
    char filename[32];    
    size_t read_len;
    
    FILE **fds; // File descriptor array
    fds = malloc(CH_NO * sizeof(*fds));
    
    uint8_t **buffers;
    buffers = malloc(CH_NO *sizeof(*buffers));
    for (int m=0; m<CH_NO; m++)
    {
        buffers[m] = malloc(BUFFER_SIZE*sizeof(**buffers));
    }
        
    for(int m=0; m< CH_NO; m++)
    {
        sprintf(filename, "_dataFiles/sim%d.iq", m);
        if((fds[m] = fopen(filename, "rb")) == NULL) {
            fprintf(stderr, "Could not open file \n");		
            success=0;
        }
    }
    if(success != 1)
        return -1;
    
    fprintf(stderr,"All files opened\n");
        
    
    for(int b=0; b<500; b++)
    {
        fprintf(stderr, "Transfering block:%d ",b);	
        usleep(1000000);
        for(int m=0; m< CH_NO; m++)
        {
            read_len = fread(buffers[m], sizeof(**buffers),BUFFER_SIZE, fds[m]);
            if(read_len != BUFFER_SIZE)
            {
                fprintf(stderr, " [ FAILED ]\n");	
                fprintf(stderr, "ERROR: Read bytes: %zu\n",read_len);	
                success = 0;
                break;
            }
            fwrite(buffers[m], sizeof(**buffers), BUFFER_SIZE, stdout);
            fflush(stdout);
        }
        if(success)
            fprintf(stderr, " [ DONE ]\n");
        else
        {
            
            break;
        }
    }
        
    
    
    /* Closing files */
    for(int m=0; m< CH_NO; m++)
    {            
        if(fclose(fds[m])==EOF)
            fprintf(stderr," File close failed closed\n");
    }
    fprintf(stderr,"All files closed\n");
        
    /* Freeing up sample buffers */
    for (int m=0; m<CH_NO; m++)
    {
        free(buffers[m]);
    }
    fprintf(stderr, "Hydra test finished\n");	
    return 0;
}
