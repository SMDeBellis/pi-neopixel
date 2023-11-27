import { Frame } from './Frame';

export interface FrameCollection {
    collectionName: string;
    collectionId: number;
    frames: [Frame];
}