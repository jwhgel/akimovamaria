#pragma once
#include "TmxLevel.h"
#include <vector>
#include <SFML/System.hpp>

struct GameView;

struct GameScene
{
    TmxLevel level;
    TmxObject player;
    std::vector<TmxObject> enemies;   // âðàãè
    std::vector<TmxObject> coins;     // ìîíåòû
    std::vector<TmxObject> blocks;    // ïðåïÿòñòâèÿ
    sf::Vector2f startPosition;       // íà÷àëüíàÿ ïîçèöèÿ èãðîêà
};

GameScene* NewGameScene();
void UpdateGameScene(void* pData, GameView& view, float deltaSec);
void DrawGameScene(void* pData, GameView& view);
void DestroyGameScene(GameScene*& pScene);