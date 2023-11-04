import { Pixel } from './Pixel';

export interface Frame{
	frame_name?: string;
	frame_index?: number;
	saved: boolean;
	pixels: [Pixel];
}
