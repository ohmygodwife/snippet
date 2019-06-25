    // 'scene' is an autorelease object
    auto scene = Scene::create();
    
    // 'layer' is an autorelease object
    HelloWorld *layer = HelloWorld::create();

    // add layer as a child to scene
    scene->addChild(layer);

    // return the scene
    return scene;
    
TransitionSlideInT

replaceScene(Scene); //旧Scene释放，省内存
pushScene/popScene;  //不常用，使用多个Layer实现

使用一张图片创建一个精灵，用于表现图像
Sprite* sprite = Sprite::create("a.png");

响应菜单，Menu和Scene一样，是虚拟概念，用于存放和管理各种子菜单，菜单类以MenuItem开头，如MenuItemLabel/MenuItemImage
auto closeItem = MenuItemImage::create(
                                        "CloseNormal.png",
                                        "CloseSelected.png",
                                        CC_CALLBACK_1(HelloWorld::menuCloseCallback,this));

Layer : Node : Ref
Node可以设置缩放/坐标/拉伸/获取大小/设置可见/schedule
触摸事件已经从Layer中抽离出来，因此Node和Layer区别很小

Value/Vector/Map
类似std::vector，会自动在添加和删除时维护元素的reference count。因此必须保证Vector和Map的value都继承自Ref！

数字与字符串转换：
Value("1235").asInt()
Value(1235).asString().c_str()

打印日志使用：log("%s%d", str, i);

播放音效：
#include "SimpleAudioEngine.h"
CocosDenshion::SimpleAudioEngine::sharedEngine()->playBackgroundMusic("a.mp3", true); //播放Resouces目录下的背景音效，第二参数表示是否重复
playEffect("error.wav"); //播放短促音效

可拉伸图片
#include "cocos-ext.h"
using namespace cocos2d::extension;
Scale9Sprite* nine = Scale9Sprite::create("a.png");
解决方案右键->添加->现有项目->cocos2d/extendsions/proj.win32/libExtensions.vcxproj
项目右键->属性->
      通用属性->添加新引用->libExtensions打勾
      配置属性->[C/C++]->常规->附加包含目录->加上$(EngineRoot)

auto pageView = level->getChildByName<ui::PageView*>("");
auto levelNumber = level->getChildByName<ui::TextAtlas*>("");
pageView->addEventListener([levelNumber, pageView](Ref* ref, ui::PageView::EventType type){
  if (type == ui::PageView::EventType::TURNING) {
    levelNumber->setString(StringUtils::format("%zd/3", pageView->getCurPageIndex() + 1));
  }
}
);

auto left = level->getChildByName<ui::Button*>();
left->addClickEventListener([pageView](Ref* ref){
  auto index = pageView->getCurPageIndex();
  index --;
  if (index < 0)
    return;
  pageView->scrollToPage(index);
});

//物理按键监听
auto listener = EventListenerKeyboard::create();
listener->onKeyReleased = [](EventKeyboard::KeyCode code, Event* event) {
  switch (code) {
    case EventKeyboard::KeyCode::KEY_BACK:
      Director::getInstance()->end();
      break;
    case EventKeyboard::KeyCode::KEY_MENU:
      log("menu");
      break;
    default:
      break;
  }
};
Director::getInstance()->getEventDispatcher()->addEventListenerWithSceneGraphPriority(listener, this);

// 声音
auto audio = root->getChildByName("audio_1");
auto a = (cocostudio::ComAudio*)audio->getComponent("audio_1");

//动画
auto root = CSLoader::createNode("main.csb");
addChild(root);
auto timeLine = CSLoader::createTimeLine("main.csb");
timeLine->gotoFrameAndPlay(0);

root->runAction(timeLine);

//帧事件
timeLine->setFrameEventCallFunc([](cocostudio::timeline::Frame* frame) {
  auto event = dynamic_cast<cocostudio::timeline::EventFrame*>(frame);
  if (event ==nullptr)
    return;
  log("%s", event->getEvent().c_str());
}
);

//plist
新建合图，所有图片移动到合图，自动裁切，最大尺寸修改，重新发布，则在res中只有plist.png

SpriteFrameCache::getInstance()->addSpriteFramesWithFile("Plist.plist");
//然后再加root
auto root = CSLoader::createNode("main.csb");

//进阶，异步加载
Director::getInstance()->getTextureCache()->addImageAsync("Plist.png", [this](Texture2D* texture){
  SpriteFrameCache::getInstance()->addSpriteFramesWithFile("Plist.plist", texture);
  auto root = CSLoader::createNode("main.csb");
  auto button = ...
  button->addClickEventListener...
  
}
);

auto btn = dynamic_cast<Node*> (ref);
if (btn != nullptr)
  log("Name: %s", btn->getName().c_str());