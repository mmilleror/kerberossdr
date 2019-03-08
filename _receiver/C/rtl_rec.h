#include <pthread.h>
#include <rtl-sdr.h>
#include <stdio.h>
struct rtl_rec_struct {
    int dev_ind, gain;
    rtlsdr_dev_t *dev;
    uint8_t *buffer;   
    unsigned long buff_ind;
    pthread_t async_read_thread;        
    uint32_t center_freq, sample_rate;
};
