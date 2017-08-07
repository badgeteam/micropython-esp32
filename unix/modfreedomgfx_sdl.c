/*
 * This file is part of the SHA2017 Micro Python fork
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2017 Christian Carlowitz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include "modfreedomgfx_sdl.h"
#include <badge_eink.h>
#include <badge_button.h>
#include <badge_input.h>
#include <SDL2/SDL.h>

SDL_Window* win;
SDL_Renderer* ren;
SDL_Texture* tex;

void freedomgfxInit(void)
{
	SDL_Init(SDL_INIT_VIDEO);
	win = SDL_CreateWindow("Freedom GFX", 100, 100, BADGE_EINK_WIDTH, BADGE_EINK_HEIGHT, SDL_WINDOW_SHOWN);
	ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
	tex = SDL_CreateTexture(ren, SDL_PIXELFORMAT_RGB332, SDL_TEXTUREACCESS_STREAMING, BADGE_EINK_WIDTH, BADGE_EINK_HEIGHT);
}

void freedomgfxDeinit(void)
{
	SDL_DestroyRenderer(ren);
	SDL_DestroyWindow(win);
	SDL_Quit();
}

uint32_t freedomgfxPoll(void)
{
	SDL_Event evt;
	if(SDL_PollEvent(&evt))
	{
		if(evt.type == SDL_KEYDOWN)
		{
			switch(evt.key.keysym.sym)
			{
			case 'a':
				return BADGE_BUTTON_A;
			case 'b':
				return BADGE_BUTTON_B;
			case 's':
				return BADGE_BUTTON_START;
			case 'S':
				return BADGE_BUTTON_SELECT;
			case SDLK_UP:
				return BADGE_BUTTON_UP;
			case SDLK_DOWN:
				return BADGE_BUTTON_DOWN;
			case SDLK_LEFT:
				return BADGE_BUTTON_LEFT;
			case SDLK_RIGHT:
				return BADGE_BUTTON_RIGHT;
			}
		}
	}
	return 0;
}

void freedomgfxDraw(uint8_t* img)
{
	uint8_t* px;
	int pitch;
	SDL_LockTexture(tex,0,(void**)&px,&pitch);
	for(int i = 0; i < BADGE_EINK_WIDTH*BADGE_EINK_HEIGHT; i++)
		px[i] = (img[i/8] & (1<<(i%8)))?0xff:0x00;
	SDL_UnlockTexture(tex);
	SDL_RenderCopy(ren,tex,0,0);
	SDL_RenderPresent(ren);
}

