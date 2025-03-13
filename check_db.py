import aiosqlite
import asyncio
import json

async def main():
    try:
        async with aiosqlite.connect('tickets.db') as db:
            db.row_factory = aiosqlite.Row
            
            # Check ticket templates
            cursor = await db.execute('SELECT * FROM ticket_templates')
            templates = await cursor.fetchall()
            print(f"Templates found: {len(templates)}")
            for t in templates:
                t_dict = dict(t)
                form_fields = json.loads(t_dict['form_fields'])
                print(f"- {t_dict['template_name']} ({t_dict['category']}): {len(form_fields)} fields")
            
            # Check ticket panels
            cursor = await db.execute('SELECT * FROM ticket_panels')
            panels = await cursor.fetchall()
            print(f"\nPanels found: {len(panels)}")
            for p in panels:
                p_dict = dict(p)
                print(f"- {p_dict['panel_name']} ({p_dict['category']}): {p_dict['question'][:30]}...")
            
            # Check guild config
            cursor = await db.execute('SELECT * FROM guild_config')
            configs = await cursor.fetchall()
            print(f"\nConfigurations found: {len(configs)}")
            for c in configs:
                c_dict = dict(c)
                config = json.loads(c_dict['config'])
                print(f"- Guild {c_dict['guild_id']}: {', '.join(config.keys())}")
                
                # Check if category_panels exists
                if 'category_panels' in config:
                    print(f"  Category panels: {config['category_panels']}")
                    
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
