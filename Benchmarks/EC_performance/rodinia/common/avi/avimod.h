#ifdef __cplusplus
extern "C" {
#endif

#define fp float

#include "avilib.h"

fp *chop_flip_image(char *image, int height, int width, int cropped, int scaled,
                    int converted);

fp *get_frame(avi_t *cell_file, int frame_num, int cropped, int scaled,
              int converted);

#ifdef __cplusplus
}
#endif
