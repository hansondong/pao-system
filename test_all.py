import asyncio
import aiohttp

async def test_worker(ws_id, ws_name, port):
    url = f'http://localhost:{port}/execute'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={
                'task_id': 'test',
                'task_type': 'echo',
                'task_params': {'msg': f'hello from {ws_id}'},
                'sender_ws': 'test'
            }) as resp:
                result = await resp.json()
                return f'{ws_name} ({port}): {result.get("result", {}).get("ws_id", "ERROR")}'
    except Exception as e:
        return f'{ws_name} ({port}): FAIL - {e}'

workers = [
    ('worker_01', '示例Agent - 技能测试', 8767),
    ('worker_02', '示例Agent - 数据查询', 8768),
    ('worker_03', '示例Agent - 通用能力', 8769),
    ('worker_04', '示例Agent - 技能验证', 8770),
    ('worker_05', '示例Agent - 团队管理', 8771),
    ('worker_06', '示例Agent - 验证助手', 8772),
    ('worker_07', '示例Agent - 开发集成', 8773),
    ('worker_08', '示例Agent - 助手服务', 8774),
]

results = asyncio.run(asyncio.gather(*[test_worker(*w) for w in workers]))
print('=' * 60)
print('跨工作区通信测试结果')
print('=' * 60)
for r in results:
    print(r)
print('=' * 60)